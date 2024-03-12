from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rollnumber = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='event_images/')
    description = models.TextField()

    def __str__(self):
        return self.name
class EventRe(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    rollnumber=models.CharField(max_length=10)
    branch=models.CharField(max_length=10)
    event=models.CharField(max_length=50)