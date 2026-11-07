# Tour Package Management System

Student: Raina Joshy  
Register Number: CCE25CS208

A Django CRUD application with signup, login, logout, and protected package-management pages.

## 1. Setup

Install Python 3.10+ and open a terminal in this folder.

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

Install Django and prepare the database:

```bash
pip install -r requirements.txt
python manage.py makemigrations packages
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## 2. First use

1. Select **Sign up** and create a username/password.
2. Log in.
3. Add, view, edit, or delete tour packages.
4. Use **Logout** to end the session.

## 3. Project structure

```text
tourproject/
    settings.py
    urls.py
    wsgi.py
    asgi.py
packages/
    migrations/
    templates/packages/
    static/packages/css/style.css
    static/packages/js/validation.js
    models.py
    forms.py
    views.py
    urls.py
```

## 4. Notes

- Package fields follow the question paper: `package_name`, `destination`, `duration`, and `price`, all as `CharField`.
- Django's built-in `UserCreationForm`, authentication views/functions, and `@login_required` are used.
- The add/edit form validates that no field is empty in both the browser and server.
- For submission, rename the outer project folder to include your name and register number if your instructor requires it.
