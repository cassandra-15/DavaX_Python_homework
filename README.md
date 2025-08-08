# 📐 Math Microservice

This project is a Python-based microservice for computing mathematical operations (power, factorial, and Fibonacci). It is built with **FastAPI**, supports **caching** via Redis, **logging** via Kafka, **monitoring** via Prometheus, and persists API requests using **SQLite**.

---

## 🚀 Features

- **FastAPI** backend for RESTful endpoints.
- **Redis** caching to avoid redundant calculations.
- **Kafka** logging of API requests.
- **Prometheus** metrics instrumentation.
- **SQLite** database for persisting API logs.
- **Dockerized** for easy deployment.

---

## 🧮 Supported Operations

| Endpoint       | Description                  | Parameters            |
|----------------|------------------------------|------------------------|
| `/power`       | Calculates base^exponent     | `base`, `exp` (int)    |
| `/factorial`   | Calculates factorial of n    | `n` (int)              |
| `/fibonacci`   | Calculates n-th Fibonacci    | `n` (int)              |

If the result of an operation exists in cache or database, it's returned immediately without recomputation.

---

## 🧰 Tech Stack

- **Backend**: FastAPI
- **Cache**: Redis
- **Database**: SQLite (via SQLAlchemy)
- **Logging**: Kafka
- **Monitoring**: Prometheus
- **Containerization**: Docker, Docker Compose

---

## 🐳 Getting Started (Docker)

### 1. Clone the repo

```bash
git clone https://github.com/cassandra-15/DavaX_Python_homework.git
cd math-microservice
```
## Build and Start Services
docker-compose up --build

## 📦 Local Development
bash:

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run app locally
uvicorn app.main:app --reload

