# AI-Powered Inventory Management System

Production-ready full-stack inventory system with clean MVC backend, normalized MySQL schema, analytics dashboard, and AI demand prediction.

## Stack
- Frontend: HTML, Bootstrap, Vanilla JS, Chart.js
- Backend: Flask REST API (modular MVC)
- Database: MySQL
- AI/ML: Scikit-learn Linear Regression

## Project Structure
- `frontend/pages` UI pages (`login`, `dashboard`, `products`, `transactions`, `reports`)
- `frontend/assets/js` API client, charts, search, config
- `backend/routes` REST routes
- `backend/controllers` business logic
- `backend/models` DB access
- `backend/ml/prediction.py` demand prediction model
- `database/schema.sql` normalized schema + seed user

## API Endpoints
- `POST /api/login`
- `GET|POST /api/products`
- `PUT|DELETE /api/products/<id>`
- `GET|POST /api/transactions`
- `GET /api/dashboard`
- `GET /api/predict/<product_id>`
- `GET /api/reports/export`

## Local Setup
1. Create database schema:
   ```bash
   mysql -u root -p < database/schema.sql
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables:
   ```bash
   export DB_HOST=localhost
   export DB_PORT=3306
   export DB_USER=root
   export DB_PASSWORD=your_password
   export DB_NAME=inventory_db
   export JWT_SECRET=change_me
   export CORS_ORIGIN=*
   ```
4. Run backend:
   ```bash
   python backend/app.py
   ```
5. Serve frontend (example):
   ```bash
   cd frontend && python -m http.server 8080
   ```
   Open `http://localhost:8080/pages/login.html`.

## Deploy
- Backend: Render (uses `Procfile` and `gunicorn`)
- Frontend: Vercel static hosting
