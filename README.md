# Community Tool Sharing Platform

A web-based platform for neighborhoods to share tools and resources, powered by quantum computing optimization (future enhancement).

## Project Overview

This project demonstrates how quantum computing can be leveraged to optimize community resource sharing. Initially, it provides a multi-page web application where neighbors can:

- Register and create profiles with their neighborhood information
- List tools and items they're willing to share
- Browse available items from other community members
- Request to borrow items
- Manage and approve/reject borrow requests
- Track borrowed items and returns

**Future Enhancement:** Integrate quantum algorithms (QAOA) to optimize resource matching based on proximity, availability, and user preferences.

## Technology Stack

- **Backend:** Flask (Python web framework)
- **Database:** SQLite (lightweight, file-based)
- **Frontend:** Vanilla JavaScript + HTML/CSS (multi-page app)
- **Quantum:** Qiskit + IBM Quantum (for future optimization features)

## Project Structure

```
.
├── quantum_connect.py          # Original IBM Quantum connection tool
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── app/
    ├── __init__.py            # Flask app initialization
    ├── main.py                # Entry point - run this to start server
    ├── models.py              # Database models (User, Item, Request)
    ├── routes.py              # Flask routes and API endpoints
    ├── static/
    │   ├── css/
    │   │   └── style.css      # Styling for all pages
    │   └── js/
    │       └── browse.js      # JavaScript for browse page
    └── templates/
        ├── base.html          # Base template with navigation
        ├── login.html         # Login page
        ├── register.html      # Registration page
        ├── dashboard.html     # User dashboard
        ├── browse.html        # Browse available items
        ├── add_item.html      # Add new item form
        ├── item_detail.html   # Single item details and request
        └── manage_requests.html # Manage incoming requests
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure IBM Quantum (Optional)

If you want to use IBM Quantum features later:

1. Get your IBM Quantum API token from [IBM Quantum](https://quantum-computing.ibm.com/)
2. Update `API_TOKEN` in `quantum_connect.py` with your actual token

### 3. Start the Application

```bash
cd app
python main.py
```

The application will be available at `http://localhost:5000`

## Usage

### Create an Account

1. Go to http://localhost:5000
2. Click "Register here"
3. Fill in your details including neighborhood information
4. Submit the registration form

### Add Items to Share

1. After logging in, click "Add Item"
2. Enter the item name, description, and category
3. Submit to list the item

### Browse and Request Items

1. Click "Browse Items" to see available items
2. Filter by category if desired
3. Click on an item to view details
4. Click "Request This Item" to send a request

### Manage Requests

1. Click "Requests" to see requests from other users
2. Approve requests to make items available for pickup
3. Reject requests to decline sharing
4. Mark items as "Returned" when they're brought back

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Redirect to login |
| GET/POST | `/login` | User login |
| GET/POST | `/register` | User registration |
| GET | `/logout` | Logout user |
| GET | `/dashboard` | User dashboard |
| GET | `/browse` | Browse available items |
| GET/POST | `/add-item` | Add new item |
| GET | `/item/<id>` | View item details |
| POST | `/request-item/<id>` | Request an item |
| GET | `/manage-requests` | Manage incoming requests |
| GET | `/api/items` | Get items (JSON API) |
| POST | `/api/request/<id>/approve` | Approve request |
| POST | `/api/request/<id>/reject` | Reject request |
| POST | `/api/request/<id>/return` | Mark item returned |

## Database Models

### User
- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `password_hash` - Hashed password
- `full_name` - User's full name
- `address` - Street address
- `neighborhood` - Neighborhood identifier
- `phone` - Optional contact number
- `created_at` - Account creation timestamp

### Item
- `id` - Primary key
- `name` - Item name
- `description` - Item description
- `category` - Category (Tools, Books, Electronics, Sports, Garden, Other)
- `owner_id` - Foreign key to User
- `available` - Availability status
- `created_at` - Item listing date
- `updated_at` - Last update date

### Request
- `id` - Primary key
- `item_id` - Foreign key to Item
- `requester_id` - Foreign key to User
- `status` - Request status (pending, approved, rejected, returned)
- `request_date` - Request submission date
- `pickup_date` - Scheduled pickup date
- `return_date` - Item return date

## Future Enhancements

### Phase 2: Quantum Optimization
- Implement QAOA algorithm for optimal resource matching
- Consider proximity, availability, and user preferences
- Reduce search time for large communities (supporting 1000+ users)

### Phase 3: Advanced Features
- Food delivery route optimization using quantum computing
- User ratings and reputation system
- Availability calendar/scheduling
- Payment processing for optional services
- Mobile app

### Phase 4: Scaling
- Replace SQLite with PostgreSQL
- Add caching with Redis
- Implement message queue for notifications
- Deploy to cloud infrastructure

## Performance Considerations

- **Current Scale:** Supports ~1000 active users with SQLite
- **Query Optimization:** Consider database indexing on neighborhood, category, available fields
- **Pagination:** Browse page could implement pagination for large item lists
- **Caching:** API responses could be cached for popular categories

## Contributing

This is a community-focused project. To contribute:

1. Test the application locally
2. Report issues and suggest improvements
3. Help optimize with quantum algorithms

## License

MIT License - Feel free to use and modify for your community

## Support

For issues or questions:
1. Check the documentation above
2. Review database schema in `models.py`
3. Examine route handlers in `routes.py`
4. Check browser console for JavaScript errors

---

## Deployment

This app is currently local-only. To publish it on a free cloud host, connect this repository to a service such as Render, Railway, or PythonAnywhere.

Recommended files for deployment:
- `Procfile` — tells the host how to start the app with Gunicorn
- `runtime.txt` — specifies the Python version
- `requirements.txt` — includes Flask, SQLAlchemy, and Gunicorn
- `wsgi.py` — cloud entry point for the app

### Example deploy flow
1. Push this repository to GitHub
2. Create a free account on Render or Railway
3. Link your GitHub repo
4. Choose Python/Flask and deploy using `wsgi:app`

**Built with ❤️ for community sharing | Powered by Quantum Computing**