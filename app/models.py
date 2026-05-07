from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    neighborhood = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    items = db.relationship('Item', backref='owner', lazy=True, cascade='all, delete-orphan')
    requests = db.relationship('Request', backref='requester', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'address': self.address,
            'neighborhood': self.neighborhood,
            'phone': self.phone
        }

class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)  # Tools, Books, Electronics, Sports, Garden, Other
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    requests = db.relationship('Request', backref='item', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'owner': self.owner.to_dict(),
            'available': self.available,
            'created_at': self.created_at.isoformat()
        }

class Request(db.Model):
    __tablename__ = 'requests'
    
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    requester_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected, returned
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    pickup_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    
    def to_dict(self):
        return {
            'id': self.id,
            'item': self.item.to_dict(),
            'requester': self.requester.to_dict(),
            'status': self.status,
            'request_date': self.request_date.isoformat(),
            'pickup_date': self.pickup_date.isoformat() if self.pickup_date else None,
            'return_date': self.return_date.isoformat() if self.return_date else None
        }
