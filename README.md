# Product Price Tracker API

A REST API for tracking product prices.

## Technologies

- **Python 3.11**
- **FastAPI** — modern, fast web framework
- **Uvicorn** — ASGI server
- **Pydantic** — data validation

## Installation

### 1. Clone the repository
```bash
git clone <repo-url>
cd product-price-tracker-api
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the API
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Project Structure

```
product-price-tracker-api/
├── main.py          # FastAPI application and endpoints
├── models.py        # SQLAlchemy database models
├── schemas.py        # Pydantic request/response schemas
├── auth.py           # Password hashing and JWT authentication
├── database.py       # SQLite database setup
├── requirements.txt  # Project dependencies
├── Dockerfile         # Docker container definition
└── README.md          # This file
```

## Authentication

Product-modifying endpoints require a JWT access token. Read-only endpoints
(`GET /products`, `GET /products/{id}`, price history) remain public.

1. Create an account: `POST /register` with `{"email": ..., "password": ...}`
2. Get a token: `POST /login` with form fields `username` (your email) and `password`
3. Send the token on protected requests: `Authorization: Bearer <access_token>`

Set the `SECRET_KEY` environment variable in production — it defaults to a
development-only value.

## API Endpoints

| Method | URL | Description | Auth required |
|--------|-----|-------------|----------------|
| GET | `/` | API health check | No |
| POST | `/register` | Create a user account | No |
| POST | `/login` | Obtain a JWT access token | No |
| POST | `/products` | Create a product | Yes |
| GET | `/products` | List products | No |
| GET | `/products/{id}` | Get a product | No |
| POST | `/products/{id}/price` | Record a new price | Yes |
| GET | `/products/{id}/price-history` | Get price history | No |
| DELETE | `/products/{id}` | Delete a product | Yes |

## Running with Docker

```bash
docker build -t price-tracker-api .
docker run -p 8000:8000 price-tracker-api
```

## Documentation

Auto-generated docs are available while the API is running:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
