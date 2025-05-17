# 📌 Remind-me-later – Django Reminder API

A simple Django-based web API that allows users to set reminders with:
- 📅 Date
- ⏰ Time
- 📝 Message
- 📤 Reminder Type (SMS / Email)

---

## 🚀 Features

- Create reminders by sending `date`, `time`, `message`, and `reminder_type`
- Supports reminder types: SMS and Email
- Stores reminder data in a SQLite database
- Admin panel access to view and manage reminders


---

## 🛠 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (default)

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

- View, edit, or delete reminders

- Add new reminders manually


## Notes
- This project does not handle sending reminders via SMS or email; it only stores the reminder data.

- The reminder_type field currently supports only "SMS" and "Email".

- Future enhancements may include other reminder delivery methods and scheduling.


📄 License
This project is licensed under the MIT License.
