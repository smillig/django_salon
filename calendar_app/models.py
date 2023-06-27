from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user since more fields are needed
class CalendarUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    GENDER_CHOICES = [
        ("-", "---"),
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other")
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone_num = models.CharField(max_length=13, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


# Create calendar object 
class Calendar(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.location


# Create Events to display on calendar
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CalendarUser, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.name
