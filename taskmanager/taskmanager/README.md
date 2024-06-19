# Task Manager

A simple Django application to manage tasks with a RESTful API and frontend.

## Requirements

- Python 3.x
- Django
- Django REST framework

## Setup

1. Install the dependencies:
    ```
    pip install django djangorestframework
    ```

2. Run the migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Start the development server:
    ```
    python manage.py runserver
    ```

4. Open your browser and go to `http://127.0.0.1:8000`.

## API Endpoints

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/<id>/` - Retrieve a task
- `PUT /api/tasks/<id>/` - Update a task
- `DELETE /api/tasks/<id>/` - Delete a task
