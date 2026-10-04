# Task Management REST API

A RESTful Task Management API built using Python, Flask, MySQL and JWT authentication.

## Technologies

- Python
- Flask
- MySQL
- JWT
- REST API
- Git & GitHub

## Features

- User registration
- User login
- Password hashing
- JWT authentication
- Create tasks
- Get all tasks
- Get task by ID
- Update task status
- Delete tasks
- User-specific task authorization
- Input validation

## API Endpoints

### Authentication

POST /users/register

POST /users/login

### Tasks

POST /tasks

GET /tasks

GET /tasks/<task_id>

PUT /tasks/<task_id>

DELETE /tasks/<task_id>

## Project Structure


task-management-api/
│
├── routes/
├── app.py
├── db.py
├── validations.py
├── requirements.txt   
├── README.md         
├── .env.example
└── .gitignore

## Authentication

JWT Bearer authentication is required for task endpoints.

## Database

MySQL is used to store users and tasks.

## Author

Tarun Sai Kumar