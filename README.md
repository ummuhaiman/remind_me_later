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
python manage.py makemigrations
python manage.py migrate
## Create a superuser for admin panel
python manage.py createsuperuser
## Run the development server
python manage.py runserver
🌐 API Endpoint
POST /api/reminders/create/
Creates a new reminder.

Request body (JSON):
{
  "date": "2025-05-17",
  "time": "15:30",
  "message": "Meeting with John",
  "reminder_type": "email"
}
Response:
{
  "id": 1,
  "date": "2025-05-17",
  "time": "15:30:00",
  "message": "Meeting with John",
  "reminder_type": "email"
}
🔐 Admin Panel
Visit: http://127.0.0.1:8000/admin/

Login using the superuser credentials you created.

From here, you can:

View, edit, or delete reminders

Add new reminders manually
📁 Project Structure
remind_me_later/
├── reminders/               # App folder
│   ├── admin.py             # Admin registration
│   ├── models.py            # Reminder model
│   ├── serializers.py       # API serializer
│   ├── views.py             # API views
│   ├── urls.py              # App URLs
├── remind_me_later/         # Main project folder
│   └── settings.py
│   └── urls.py
├── db.sqlite3               # SQLite database
├── manage.py
├── requirements.txt
└── README.md
📄 License
This project is licensed under the MIT License.
