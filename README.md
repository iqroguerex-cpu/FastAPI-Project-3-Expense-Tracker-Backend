# ⚡ Expense Tracker API (FastAPI Backend)

[![Live API](https://img.shields.io/badge/Live-API-success?style=for-the-badge\&logo=fastapi)](https://fastapi-project-3-expense-tracker-backend.onrender.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://python.org)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge\&logo=render\&logoColor=white)](https://render.com/)
[![API Docs](https://img.shields.io/badge/API%20Docs-Swagger-green?style=for-the-badge)](https://fastapi-project-3-expense-tracker-backend.onrender.com/docs)

A **high-performance REST API** built with **FastAPI** for managing personal expense data.

The API powers the **Expense Tracker Dashboard** and provides endpoints for **creating, retrieving, updating, and deleting expenses**.

---

# 🌐 Live API

### Base URL

https://fastapi-project-3-expense-tracker-backend.onrender.com

### Interactive API Documentation

Swagger UI
https://fastapi-project-3-expense-tracker-backend.onrender.com/docs

ReDoc
https://fastapi-project-3-expense-tracker-backend.onrender.com/redoc

---

# ✨ Features

* ⚡ **FastAPI performance**
* 📚 **Auto-generated Swagger documentation**
* 🔄 **Full CRUD operations**
* 🌐 **CORS enabled for frontend apps**
* 🧩 **Lightweight in-memory storage**
* 🚀 **Deployed on Render**

> Note: Data resets when the server restarts since the current version uses in-memory storage.

---

# 🏗 Architecture

```id="j70b6v"
Streamlit Dashboard
        │
        ▼
 FastAPI Backend
        │
        ▼
 In-Memory Expense Store
```

Future improvements could include:

* PostgreSQL database
* authentication system
* user accounts
* budget alerts

---

# 📡 API Endpoints

| Method   | Endpoint                        | Description            |
| -------- | ------------------------------- | ---------------------- |
| `GET`    | `/expenses`                     | Get all expenses       |
| `GET`    | `/expenses/{id}`                | Get a specific expense |
| `POST`   | `/expenses/create_expense`      | Create a new expense   |
| `PUT`    | `/expenses/update_expense/{id}` | Update an expense      |
| `DELETE` | `/expenses/delete_expense/{id}` | Delete an expense      |

---

# 📥 Example Request

### Create Expense

```id="lo5xbr"
POST /expenses/create_expense
```

Request Body

```json
{
  "id": 101,
  "title": "Groceries",
  "amount": 52.40,
  "category": "food",
  "date": "2026-03-10"
}
```

Response

```json
"Expense Added Successfully"
```

---

# 📂 Project Structure

```id="23q1b0"
expense-tracker-backend
│
├── expense_api.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Local Development

Clone the repository

```id="qr6y4o"
git clone https://github.com/iqroguerex-cpu/fastapi-project-3-expense-tracker-backend
```

Navigate to the project

```id="8c8j2d"
cd fastapi-project-3-expense-tracker-backend
```

Install dependencies

```id="mvywo0"
pip install -r requirements.txt
```

Run the server

```id="gnvl9g"
uvicorn expense_api:app --reload --port 8002
```

Open the API documentation

```id="4dy8sl"
http://127.0.0.1:8002/docs
```

---

# 🔗 Frontend Dashboard

The Streamlit dashboard for this API:

Frontend Repository
https://github.com/iqroguerex-cpu/fastapi-project-3-expense-tracker-frontend

---

# 📄 License

This project is released under the **MIT License**.

---

# 👨‍💻 Author

**Chinmay V Chatradamath**

GitHub
https://github.com/iqroguerex-cpu

---

⭐ If you found this project useful, consider **starring the repository**.
