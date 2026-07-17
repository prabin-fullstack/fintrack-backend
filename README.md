# Fintrack — Backend

Django REST Framework backend for **Fintrack**, a full-stack personal
finance tracker. Implements JWT authentication and RESTful APIs for
transactions, categories, and payment methods, backed by a production
Neon PostgreSQL database.

🔗 **Frontend Repo:** https://github.com/prabin-fullstack/fintrack-frontend
🔗 **Live Demo:** https://fintrack-frontend-liart.vercel.app

## Features
- JWT-based authentication and authorization
- CRUD APIs for income/expense transactions
- Category and payment method management
- Analytics endpoints powering the dashboard's income/expense breakdowns

## Tech Stack
Python · Django · Django REST Framework · Simple JWT · PostgreSQL (Neon)

## Folder Structure
```
fintrack-backend/
├── accounts/          # User auth & JWT logic
├── transactions/      # Transaction CRUD + models
├── expense_tracker/   # Project settings
├── manage.py
└── requirements.txt
```

## Installation
```bash
git clone https://github.com/prabin-fullstack/fintrack-backend.git
cd fintrack-backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Environment Variables
Create a `.env` file in the root:
```
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@host:port/dbname
```

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | Obtain JWT token pair |
| POST | `/api/auth/refresh/` | Refresh access token |
| GET/POST | `/api/transactions/` | List / create transactions |
| GET/PUT/DELETE | `/api/transactions/<id>/` | Retrieve, update, delete a transaction |
| GET | `/api/analytics/summary/` | Income vs. expense summary data |

*(Adjust to match your actual `urls.py` routes)*

## Screenshots
*(Add: Postman/Thunder Client screenshot of API responses)*

## Future Improvements
- Add pagination on transaction list endpoint
- Add unit tests (pytest / Django TestCase)
- Add API rate limiting

## License
MIT
