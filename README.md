# Urban Delivery Dashboard

Containerized analytics dashboard for urban delivery operations. The project pairs a lightweight FastAPI backend with a Streamlit dashboard so delivery metrics can be explored locally or deployed as separate services.

## What It Shows

- Backend/frontend service split with Docker Compose.
- FastAPI service for operational data.
- Streamlit dashboard for business-facing delivery insights.
- Simple deployment shape that can be extended with managed databases, auth, and observability.

## Project Structure

urban-delivery-dashboard/
  backend/
    main.py
    Dockerfile
  frontend/
    dashboard.py
    Dockerfile
  docker-compose.yml

## Run

docker compose up --build

Open:

- Backend: http://127.0.0.1:8000
- Dashboard: http://127.0.0.1:8501

## Local Syntax Check

python3 -m py_compile backend/main.py frontend/dashboard.py

## Author

Krishna Mankali
