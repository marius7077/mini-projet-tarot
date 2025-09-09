# Projet TAROT

Mini-projet pour la gestion des centres d’observation, télescopes, employés et événements astronomiques.

---

## Installation

### 1. Backend Django

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python api/populate_data.py
python manage.py runserver

### 2. Frontend Vue.js 3

cd frontend
npm install
npm run dev

Le frontend sera accessible sur http://localhost:5173/

le Backend :
  http://127.0.0.1:8000/api/centers/
  http://127.0.0.1:8000/api/telescopes/
  http://127.0.0.1:8000/api/employees/
  http://127.0.0.1:8000/api/events/
