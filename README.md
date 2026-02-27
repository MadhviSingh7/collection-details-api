# Collection Details API

A lightweight FastAPI + MongoDB application for managing databases, collections, and documents.

This project provides REST APIs to browse MongoDB data and perform CRUD operations using a structured architecture.

-------------------------------------

Features

- List MongoDB databases
- List collections
- Fetch documents
- Create documents
- Update documents
- Soft delete documents
- Automatic Employee ID generation
- Request logging middleware

-------------------------------------

Technology Stack

- FastAPI
- MongoDB
- PyMongo
- Uvicorn
- Python

-------------------------------------

Project Structure

Collection_details/

main.py  
requirements.txt  
README.md  

script/
 └── core/
     ├── handlers/
     ├── services/
     ├── utilities/
     └── constants/

-------------------------------------

Installation

1) Create Virtual Environment

python -m venv .venv

Activate:

Windows:

.venv\Scripts\activate

-------------------------------------

2) Install Packages

pip install -r requirements.txt

-------------------------------------

MongoDB Configuration

File:

script/core/utilities/db.py

Default:

mongodb://localhost:27017

Make sure MongoDB is running.

-------------------------------------

Run Application

uvicorn main:app --reload --port 8004

Open Browser:

http://localhost:8004/docs

-------------------------------------

API Endpoints

GET /databases  
GET /collections?db_name=test  
GET /data?db_name=test&collection=employee  
POST /data  
PUT /data/{id}  
DELETE /data/{id}

-------------------------------------

Special Features

Automatic Employee ID:

emp_101
emp_102
emp_103

-------------------------------------

Soft Delete

Documents are not permanently deleted.

is_deleted = true

-------------------------------------

Author

Madhvi Singh