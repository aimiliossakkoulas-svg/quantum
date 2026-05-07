# Community Tool Sharing Platform - Development Guide

## Project Overview
A web-based platform for neighborhoods to share tools and resources, with future quantum computing optimization for resource matching and delivery route optimization.

## Architecture

### Backend Stack
- **Framework:** Flask (Python)
- **Database:** SQLite (community_sharing.db)
- **Authentication:** Session-based with password hashing
- **API:** RESTful endpoints for item management and requests

### Frontend Stack
- **Pages:** Multi-page HTML templates with Jinja2
- **Styling:** Vanilla CSS with responsive design
- **Interactivity:** Vanilla JavaScript (no frameworks)
- **Features:** Category filtering, dynamic item loading

### Quantum Integration (Future)
- **Framework:** Qiskit + IBM Quantum Runtime
- **Use Cases:**
  - QAOA for optimal resource matching
  - VRP solver for delivery route optimization
  - Community-scale problem optimization (1000+ users)

## Key Features

### Current (Phase 1)
1. **User Management**
   - Registration with neighborhood information
   - Secure login/logout with password hashing
   - User profiles with contact information

2. **Item Sharing**
   - Add items to share (category-based)
   - Browse available items with filtering
   - View item details and owner information

3. **Request Management**
   - Request items from other users
   - Approve/reject incoming requests
   - Track borrowed items
   - Mark items as returned

### Planned (Phase 2-4)
- Quantum-optimized resource matching
- Delivery route optimization
- User ratings and reputation
- Scheduling/calendar system
- Mobile app

## Database Schema

### Users Table
- id, username, email, password_hash
- full_name, address, neighborhood
- phone, created_at

### Items Table
- id, name, description, category
- owner_id, available, created_at, updated_at

### Requests Table
- id, item_id, requester_id, status
- request_date, pickup_date, return_date

## Development Workflow

### Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Start the Flask development server
cd app
python main.py
```

Server runs on: `http://localhost:5000`

### Database Management

```bash
# The database is automatically created on first run
# Location: app/community_sharing.db

# To reset the database:
# Simply delete app/community_sharing.db and restart the app
```

### Code Organization

```
app/
├── __init__.py        - Flask app factory
├── main.py           - Entry point
├── models.py         - SQLAlchemy models
├── routes.py         - Route handlers and API
├── templates/        - HTML templates
│   ├── base.html     - Base layout
│   ├── login.html    - Auth pages
│   ├── register.html
│   ├── dashboard.html - User dashboard
│   ├── browse.html   - Item browsing
│   ├── add_item.html - Create item
│   ├── item_detail.html
│   └── manage_requests.html
└── static/
    ├── css/
    │   └── style.css - All styling
    └── js/
        └── browse.js - Frontend interactions
```

## Key Files and Their Purposes

| File | Purpose |
|------|---------|
| `models.py` | Database schema and ORM models |
| `routes.py` | Flask route handlers, business logic |
| `__init__.py` | App initialization, database setup |
| `templates/base.html` | Navigation and layout template |
| `static/css/style.css` | All application styling |
| `static/js/browse.js` | Dynamic item loading/filtering |

## Common Development Tasks

### Adding a New Feature

1. **Database Change:** Update `models.py`
2. **API Endpoint:** Add route in `routes.py`
3. **Frontend Page:** Create template in `templates/`
4. **Styling:** Add CSS to `static/css/style.css`
5. **Interaction:** Add JS in `static/js/` if needed

### Debugging Tips

1. **Check Flask logs:** Look at terminal output for stack traces
2. **Browser console:** Check for JavaScript errors (F12)
3. **Database:** Examine `app/community_sharing.db` with SQLite viewer
4. **Session issues:** Check cookies in browser dev tools

### Testing Routes

```bash
# Login endpoint
curl -X POST http://localhost:5000/login

# Get items API
curl http://localhost:5000/api/items?category=Tools

# Approve request
curl -X POST http://localhost:5000/api/request/1/approve
```

## Future Quantum Integration

### Phase 2: Quantum Optimization

**Goal:** Use QAOA to find optimal resource matching

```python
# Pseudo-code for future implementation
from qiskit import QuantumCircuit
from qiskit.algorithms import QAOA

def find_optimal_matches(requests, available_items, user_locations):
    """Use quantum optimization for resource matching"""
    # Convert to Hamiltonian
    # Run QAOA on IBM Quantum
    # Return optimal matching
```

**Advantages:**
- Faster than classical for large communities
- Better optimization for 1000+ users
- Scales well as community grows

### Phase 3: Delivery Route Optimization

**Goal:** QAOA for Vehicle Routing Problem

```python
def optimize_delivery_routes(pickup_locations, user_neighborhoods):
    """Quantum VRP solver for route optimization"""
    # Define cost function
    # Run QAOA
    # Return optimal routes
```

## Deployment Checklist

- [ ] Change SECRET_KEY in production
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS
- [ ] Set up user authentication with OAuth
- [ ] Add rate limiting
- [ ] Set up logging and monitoring
- [ ] Configure email notifications
- [ ] Deploy to cloud (Heroku, AWS, etc.)

## Performance Targets

- **Users:** 1000 concurrent users
- **Items:** 5000+ items
- **Requests:** Sub-second response times
- **Search:** Filtered results in <500ms

## Contributing Guidelines

1. Follow PEP 8 for Python code
2. Use meaningful variable names
3. Comment complex logic
4. Test all routes before commit
5. Update documentation
6. Check for SQL injection vulnerabilities

## Security Considerations

1. **Password Security:** Use `werkzeug.security` (already implemented)
2. **SQL Injection:** Use SQLAlchemy ORM (prevents injection)
3. **CSRF Protection:** Add CSRF tokens to forms
4. **User Authorization:** Verify user owns resource before modifying
5. **Input Validation:** Sanitize all user inputs
6. **Session Management:** Use secure session cookies

## Resources

- Flask Documentation: https://flask.palletsprojects.com/
- SQLAlchemy ORM: https://docs.sqlalchemy.org/
- Qiskit Documentation: https://qiskit.org/documentation/
- IBM Quantum: https://quantum-computing.ibm.com/

---

**Last Updated:** May 2026
**Version:** 1.0
**Status:** MVP Complete, Ready for Phase 2

EXTENSION INSTALLATION RULES:
- Only install extension specified by the get_project_setup_info tool. DO NOT INSTALL any other extensions.

PROJECT CONTENT RULES:
- If the user has not specified project details, assume they want a "Hello World" project as a starting point.
- Avoid adding links of any type (URLs, files, folders, etc.) or integrations that are not explicitly required.
- Avoid generating images, videos, or any other media files unless explicitly requested.
- If you need to use any media assets as placeholders, let the user know that these are placeholders and should be replaced with the actual assets later.
- Ensure all generated components serve a clear purpose within the user's requested workflow.
- If a feature is assumed but not confirmed, prompt the user for clarification before including it.
- If you are working on a VS Code extension, use the VS Code API tool with a query to find relevant VS Code API references and samples related to that query.

TASK COMPLETION RULES:
- Your task is complete when:
  - Project is successfully scaffolded and compiled without errors
  - copilot-instructions.md file in the .github directory exists in the project
  - README.md file exists and is up to date
  - User is provided with clear instructions to debug/launch the project

Before starting a new task in the above plan, update progress in the plan.
- Work through each checklist item systematically.
- Keep communication concise and focused.
- Follow development best practices.