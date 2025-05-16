# 📌 Remind-me-later – Django Reminder API

A simple Django-based web API that allows users to set reminders with:
- 📅 Date
- ⏰ Time
- 📝 Message
- 📤 Reminder Type (SMS / Email)

---

## 🚀 Features

- Create and store reminders
- Admin panel to manage reminders
- Designed to support future reminder types

---

## 🛠 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework

---
## Apply migrations
```text
python manage.py makemigrations
```
```text
python manage.py migrate
```
## Create a superuser for admin panel
```text
python manage.py createsuperuser
```
## Run the development server
```text
python manage.py runserver
```
## 🌐 API Usage

### ➤ Endpoint: `POST /api/reminders/create/`

**Request Body (JSON):**

```json
{
  "date": "2025-05-17",
  "time": "15:30",
  "message": "Meeting with John",
  "reminder_type": "email"
}
```
**Response:**
```json
{
  "id": 1,
  "date": "2025-05-17",
  "time": "15:30:00",
  "message": "Meeting with John",
  "reminder_type": "email"
}
```

🔐 Admin Panel
Visit: http://127.0.0.1:8000/admin/

Login using the superuser credentials you created.

From here, you can:

View, edit, or delete reminders

Add new reminders manually
## 📁 Project Structure
```text
remind_me_later/          # Django project root
├── manage.py             # Django command-line utility
├── requirements.txt      # Python package dependencies
├── db.sqlite3            # Default SQLite database

├── remind_me_later/      # Main project settings
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # Root URL configurations
│   └── wsgi.py

├── reminders/            # App for handling reminders
│   ├── __init__.py
│   ├── admin.py          # Admin registration for Reminder model
│   ├── apps.py
│   ├── models.py         # Reminder model definition
│   ├── serializers.py    # DRF serializer for Reminder
│   ├── views.py          # API endpoint views
│   ├── urls.py           # App-specific URL routing
│   └── migrations/       # Auto-generated database migrations
│       └── __init__.py

└── README.md             # Project overview and usage
```
📄 License
This project is licensed under the MIT License.
