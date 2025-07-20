# Django Messaging API

A RESTful messaging API built with Django and Django REST Framework (DRF). It allows users to initiate conversations, send messages, and view chat histories. Built as part of the ALX Backend Specialization.

---

## 📦 Features

- User registration and listing
- Conversation creation between users
- Messaging within conversations
- RESTful API with browsable interface
- Swagger UI for API documentation

---

## 🛠️ Technologies Used

- Python 3.13
- Django 5.2.4
- Django REST Framework (DRF)
- drf-yasg (Swagger API docs)
- SQLite3 (default Django DB)

---

## 📁 Project Structure

messaging_app/
├── chats/
│ ├── migrations/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── messaging_app/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── README.md

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/messaging_app.git
   cd messaging_app
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Run the server

bash
Copy
Edit
python manage.py runserver
🔗 API Endpoints
Method	Endpoint	Description
GET	/api/users/	List all users
POST	/api/conversations/	Create a new conversation
GET	/api/conversations/	List all conversations
GET	/api/messages/	List all messages
POST	/api/messages/	Send a new message
GET	/swagger/	View Swagger API docs

🔍 Swagger UI
Visit http://127.0.0.1:8000/swagger/ to view the API documentation.

