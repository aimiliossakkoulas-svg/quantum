from flask import render_template, request, redirect, url_for, jsonify, session
from werkzeug.security import generate_password_hash
from .models import db, User, Item, Request
from datetime import datetime

def register_routes(app):
    
    @app.route('/')
    def index():
        return redirect(url_for('login'))
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            data = request.form
            
            if User.query.filter_by(username=data.get('username')).first():
                return render_template('register.html', error='Username already exists')
            
            if User.query.filter_by(email=data.get('email')).first():
                return render_template('register.html', error='Email already exists')
            
            user = User(
                username=data.get('username'),
                email=data.get('email'),
                full_name=data.get('full_name'),
                address=data.get('address'),
                neighborhood=data.get('neighborhood'),
                phone=data.get('phone')
            )
            user.set_password(data.get('password'))
            
            db.session.add(user)
            db.session.commit()
            
            return redirect(url_for('login'))
        
        return render_template('register.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            data = request.form
            user = User.query.filter_by(username=data.get('username')).first()
            
            if user and user.check_password(data.get('password')):
                session['user_id'] = user.id
                session['username'] = user.username
                return redirect(url_for('dashboard'))
            
            return render_template('login.html', error='Invalid credentials')
        
        return render_template('login.html')
    
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))
    
    @app.route('/dashboard')
    def dashboard():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        user = User.query.get(session['user_id'])
        user_items = Item.query.filter_by(owner_id=user.id).all()
        user_requests = Request.query.filter_by(requester_id=user.id).all()
        
        return render_template('dashboard.html', user=user, items=user_items, requests=user_requests)
    
    @app.route('/browse')
    def browse():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        user = User.query.get(session['user_id'])
        items = Item.query.filter(Item.owner_id != user.id, Item.available == True).all()
        
        return render_template('browse.html', items=items, user=user)
    
    @app.route('/add-item', methods=['GET', 'POST'])
    def add_item():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        if request.method == 'POST':
            data = request.form
            item = Item(
                name=data.get('name'),
                description=data.get('description'),
                category=data.get('category'),
                owner_id=session['user_id'],
                available=True
            )
            db.session.add(item)
            db.session.commit()
            
            return redirect(url_for('dashboard'))
        
        return render_template('add_item.html')
    
    @app.route('/item/<int:item_id>')
    def view_item(item_id):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        item = Item.query.get_or_404(item_id)
        return render_template('item_detail.html', item=item)
    
    @app.route('/request-item/<int:item_id>', methods=['POST'])
    def request_item(item_id):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        item = Item.query.get_or_404(item_id)
        
        # Check if user already has pending request
        existing = Request.query.filter_by(item_id=item_id, requester_id=session['user_id'], status='pending').first()
        if existing:
            return jsonify({'error': 'You already have a pending request for this item'}), 400
        
        new_request = Request(
            item_id=item_id,
            requester_id=session['user_id']
        )
        db.session.add(new_request)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Request sent!'})
    
    @app.route('/manage-requests')
    def manage_requests():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        
        user = User.query.get(session['user_id'])
        received_requests = Request.query.filter(
            Request.item_id.in_(db.session.query(Item.id).filter_by(owner_id=user.id))
        ).all()
        
        return render_template('manage_requests.html', requests=received_requests)
    
    @app.route('/api/request/<int:request_id>/approve', methods=['POST'])
    def approve_request(request_id):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        
        req = Request.query.get_or_404(request_id)
        item = req.item
        
        if item.owner_id != session['user_id']:
            return jsonify({'error': 'Unauthorized'}), 401
        
        req.status = 'approved'
        item.available = False
        db.session.commit()
        
        return jsonify({'success': True})
    
    @app.route('/api/request/<int:request_id>/reject', methods=['POST'])
    def reject_request(request_id):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        
        req = Request.query.get_or_404(request_id)
        item = req.item
        
        if item.owner_id != session['user_id']:
            return jsonify({'error': 'Unauthorized'}), 401
        
        req.status = 'rejected'
        db.session.commit()
        
        return jsonify({'success': True})
    
    @app.route('/api/request/<int:request_id>/return', methods=['POST'])
    def return_item(request_id):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        
        req = Request.query.get_or_404(request_id)
        
        if req.requester_id != session['user_id']:
            return jsonify({'error': 'Unauthorized'}), 401
        
        req.status = 'returned'
        req.return_date = datetime.utcnow()
        req.item.available = True
        db.session.commit()
        
        return jsonify({'success': True})
    
    @app.route('/api/items')
    def get_items():
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        
        category = request.args.get('category')
        search = request.args.get('search', '').strip()
        query = Item.query.filter(Item.owner_id != session['user_id'], Item.available == True)
        
        if category and category != 'all':
            query = query.filter_by(category=category)
        
        if search:
            search_pattern = f"%{search}%"
            query = query.filter(Item.name.ilike(search_pattern))
        
        items = query.all()
        return jsonify([item.to_dict() for item in items])
