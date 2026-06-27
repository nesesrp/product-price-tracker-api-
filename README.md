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
├── models.py        # Pydantic data models
├── database.py      # Temporary in-memory database
├── requirements.txt # Project dependencies
├── Dockerfile       # Docker container definition
└── README.md        # This file
```

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | API health check |

## Running with Docker

```bash
docker build -t price-tracker-api .
docker run -p 8000:8000 price-tracker-api
```

## Documentation

Auto-generated docs are available while the API is running:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
