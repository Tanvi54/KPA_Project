📄 README - KPA Backend

✅Project Overview
This project implements 2 API endpoints based on the KPA Form Data Postman Collection using FastAPI and PostgreSQL.

🔧 Tech Stack
FastAPI (Backend)
PostgreSQL (Database)
SQLAlchemy (ORM)
Pydantic (Schema validation)
Uvicorn (ASGI server)
Postman (Testing)

📂 Folder Structure
pgsql
Copy
Edit
kpa_backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       ├── bogie_checksheet.py
│       └── wheel_specifications.py
├── .env
├── requirements.txt
├── README.md

🚀 How to Run
1. Clone the repo or unzip the project
2. Set up a PostgreSQL DB named kpa_db
3. Add .env file:
bash
Copy
Edit
DATABASE_URL=postgresql://postgres:<password>@localhost:5432/kpa_db

4.Create virtual environment:
bash
Copy
Edit
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

5.Run:
bash
Copy
Edit
uvicorn app.main:app --reload

6.Open browser at:
bash
Copy
Edit
http://localhost:8000/docs

📬 APIs Implemented
1. POST /api/forms/bogie-checksheet
Save bogie inspection data
2. GET /api/forms/wheel-specifications
Retrieve all wheel spec entries

🧪 Testing
Use Postman to:
Send POST request with JSON body
Send GET request to fetch saved records
