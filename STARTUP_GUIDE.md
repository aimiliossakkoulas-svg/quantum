# Quick Start Guide

## 🚀 Get the App Running in 2 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start the Server
```bash
cd app
python main.py
```

### Step 3: Open in Browser
```
http://localhost:5000
```

---

## 🎯 First Time Setup

### Create Test Account
1. Click "Register here"
2. Fill in your details:
   - **Username:** testuser1
   - **Email:** test@example.com
   - **Password:** password123
   - **Full Name:** Test User
   - **Address:** 123 Main St
   - **Neighborhood:** Downtown
   - **Phone:** (optional)

### Add an Item
1. Go to Dashboard
2. Click "+ Add Item"
3. Fill in:
   - **Name:** Power Drill
   - **Description:** 20V DeWalt, great condition
   - **Category:** Tools
4. Submit

### Create Another Account to Test
1. Repeat registration with different username
2. Go to "Browse Items"
3. See the item from first user
4. Click on it and request to borrow
5. Switch back to first account
6. Go to "Requests"
7. Approve the request

---

## 📁 Project Structure

```
.
├── app/                           # Main Flask application
│   ├── main.py                   # ▶️ START HERE
│   ├── models.py                 # Database schema
│   ├── routes.py                 # All endpoints
│   ├── templates/                # HTML pages
│   └── static/                   # CSS & JavaScript
├── quantum_connect.py            # IBM Quantum connector
├── requirements.txt              # Python packages
└── README.md                     # Full documentation
```

---

## 🗄️ Database

- **Location:** `app/community_sharing.db`
- **Auto-created:** Yes, on first run
- **Reset:** Delete the .db file and restart

---

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### "Address already in use"
Server is already running. Either:
- Stop the other instance
- Or change port in `app/main.py` (port=5000 → port=5001)

### Database errors
```bash
# Delete the database
rm app/community_sharing.db
# Restart app - it will recreate
```

---

## 📚 Features

- ✅ Register & Login
- ✅ Add items to share
- ✅ Browse neighborhood items
- ✅ Request items
- ✅ Manage requests
- ✅ Track borrowed items
- 🔜 Quantum optimization (Phase 2)

---

## 🛠️ Development

### Add a New Page
1. Create HTML template in `app/templates/`
2. Add route in `app/routes.py`
3. Add CSS to `app/static/css/style.css`
4. Add navigation link in `base.html`

### Deploying Later
This project includes deployment files for free hosts:
- `Procfile`
- `runtime.txt`
- `wsgi.py`

When you're ready, push the repo to GitHub and connect it to Render, Railway, or another free Flask host.

### Debug Mode
Already enabled. Check terminal for errors when browsing.

### Database Queries
Use any SQLite viewer to inspect `app/community_sharing.db`

---

## 🎓 Next Steps

1. **Create test data** - Add several items
2. **Test workflows** - Try requesting items
3. **Explore code** - Read `routes.py` and `models.py`
4. **Phase 2 planning** - Review quantum optimization in copilot-instructions.md

---

## 📞 Support

Check full documentation:
- `README.md` - Complete guide
- `.github/copilot-instructions.md` - Development guide
- `app/routes.py` - All available endpoints
- `app/models.py` - Database schema

---

**Happy sharing! 🛠️**
