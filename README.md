# Django User Management System

Это веб-приложение на Django, предназначенное для управления списком пользователей. Приложение поддерживает аутентификацию, регистрацию, CRUD-операции для пользователей, а также предоставляет RESTful API для получения данных в формате JSON.

## Возможности

- Регистрация новых пользователей
- Аутентификация и выход из системы
- Просмотр, поиск, редактирование и удаление пользователей
- JSON API для получения списка пользователей

## Установка

1. **Клонируйте репозиторий**

```bash
git clone https://github.com/Evgeniya-321/myproject.git
cd myproject

python -m venv venv
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

myproject/
├── main/
│   ├── templates/main
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── forms.py
├── myproject/
│   ├── asgi.py
│   ├── wsgi.py
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py

Требования

Python 3.8+

Django 4.x+
