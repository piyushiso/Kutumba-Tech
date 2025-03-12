# EMIS (Employee Management Information System)

The **Employee Management Information System (EMIS)** is a Django-based web application designed to manage employee data, including user authentication, employee records, and more.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Folders 101](#folders-101)
5. [API Documentation/Walkthrough](#api-documentation)
6. [Contact](#contact)
---

## Features
- **User Authentication**: Register, login, and logout functionality with tokens.
- **Employee Management**: Managing employee records with CRUD functionality.

---

## Technologies Used
- **Backend**: Django with Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Frontend**: HTML
- **Other Tools**: `psycopg2` (PostgreSQL adapter)

---

## Setup Instructions

### Step 0: Prerequisites
- Python 3.12+
- PostgreSQL
- pip (Python package manager)
---

### Step 1: Clone the Repository
```bash
git clone https://github.com/piyushiso/Kutumba-Tech.git
cd Kutumba-Tech/emis
```
> **Note:** *Kutumba-Tech* is a master repository home to multiple projects.
---

### Step 2: Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
---

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt 

# Will automatically install all the required dependencies as listed in the requirements.txt file.
```
---

### Step 4: Database Setup
The current database configuration in emis/settings.py is as:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'emis',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Create a PostgreSQL database accordingly or use an existing one and update it as:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DATABASE_NAME',
        'USER': 'DATABASE_USER',
        'PASSWORD': 'DATABASE_PASSWORD',
        'HOST': 'localhost',
        'PORT': 'PORT',
    }
}
```
---

### Step 5: Manage Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
---

### Step 6: Create Superuser
```bash
python manage.py createsuperuser
# Follow the steps accordingly. For ease use these settings - username: admin, email: admin@example.com, password: admin, value: y.
```
---

### Step 7: Run the Development Server
```bash
python manage.py runserver
```
---

## Folders 101
```
emis (root)/
├── manage.py
├── EmployeeMIS (core)/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── employees (employee records)/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
├── users (login/register)/
│   ├── templates (frontend) /
|   |   └── dashboard (related to dashboards)
|   |       └── dashboard.html (Dashboard design)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
├── requirements.txt
├── README.md
└── .env  # For environment variables
```
---
## API Documentation

The EMIS API provides the following endpoints:

### 1. Authentication

Register: POST .../register/

Login: POST .../login/

Logout: POST .../logout/

Dashboard: POST .../dashboard/

### 2. Employee Management

List Employees: GET .../employees/

Create Employee: POST .../employees/

Retrieve Employee: GET .../employees/{id}/

Update Employee: PUT .../employees/{id}/

Delete Employee: DELETE .../employees/{id}/

---

### Contact
For questions or feedback, please contact:


**Email:** piyushshrestha20@gmail.com | piyushdoeswork@gmail.com
**GitHub:** [piyushiso](https://github.com/piyushiso)
