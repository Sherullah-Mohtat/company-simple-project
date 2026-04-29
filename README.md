<h1 align="center">Company Simple Project</h1>

<p align="center">
Production-style Django REST Framework project with JWT authentication, PostgreSQL / SQLite support, split settings architecture, templates, and customized admin panel.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Django-6.x-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/DRF-REST-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/SQLite-Lightweight-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#project-structure">Structure</a> •
  <a href="#installation">Install</a> •
  <a href="#api-docs">API Docs</a> •
  <a href="#Screenshots">Screenshots</a>
</p>

---

## Overview

Company Simple Project is a professional Django REST Framework backend project built to demonstrate modern backend engineering practices including authentication, database flexibility, modular settings, templates, and admin customization.

---

## Features

- 🔐 JWT Authentication using SimpleJWT
- 🐘 PostgreSQL Support
- 💾 SQLite Support
- ⚙️ Split Settings (`base.py`, `dev.py`, `prod.py`)
- 📘 Swagger / OpenAPI Documentation
- 🏢 Companies Module
- 👨‍💼 Employees Module
- 🎨 Customized Django Admin Panel
- 🌐 HTML Templates
- 🔒 Environment Variables with `.env`
- 📂 GitHub Ready Structure

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- SQLite
- SimpleJWT
- drf-spectacular
- django-filter
- Jazzmin Admin Theme

---

## Project Structure

```text
 ── api/
│   ├── admin/
│   ├── migrations/
│   ├── models/
│   ├── serializers/
│   ├── templates/
│   ├── tests/
│   ├── views/
│   └── urls.py
│
│── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
│
│── .env.example
│── .gitignore
│── manage.py
│── requirements.txt
│── README.md
```

---

## Installation

```bash
git clone https://github.com/Sherullah-Mohtat/company-simple-project.git
cd company-simple-project

python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env

python manage.py migrate
python manage.py runserver
```

---

## Example .env

```env
DJANGO_SETTINGS_MODULE=config.settings.dev
DEBUG=True

SECRET_KEY=change-me

DB_ENGINE=sqlite
DB_NAME=db.sqlite3

# PostgreSQL Example
# DB_ENGINE=postgres
# DB_NAME=company_db
# DB_USER=postgres
# DB_PASSWORD=yourpassword
# DB_HOST=127.0.0.1
# DB_PORT=5432
```

---

## Run Project

```text
http://127.0.0.1:8000/
```

---

## API Docs

Swagger UI:

```text
http://127.0.0.1:8000/api/docs/
```

---

## Screenshots

![Home](images/index_page.png)

![Companies](images/companies.png)

![Employees](images/employees.png)

![Admin](images/admin1.png)

![Admin](images/admin2.png)

![Swagger](images/api_docs.png)



---

## Author

**Sherullah Mohtat**

https://github.com/Sherullah-Mohtat/company-simple-project.git

---

## License

MIT Licen
