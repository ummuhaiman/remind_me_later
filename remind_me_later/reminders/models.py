from django.db import models

class Reminder(models.Model):
    REMINDER_CHOICES = (
        ('SMS', 'SMS'),
        ('Email', 'Email'),
    )
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_CHOICES)

    def __str__(self):
        return f"{self.date} {self.time} - {self.reminder_type}"
