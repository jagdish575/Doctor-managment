from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField() 
    experience = models.IntegerField()
    image = models.ImageField(upload_to="signup")

    def __str__(self):
        return self.name
    

    class Appointment(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField(unique=True)
        phone_number = models.IntegerField()
        docotor=models.CharField(max_length=200)
        date_time=models.DateTimeField(blank=False)
        Time=models.IntegerField()
        Description=models.CharField(max_length=500)


        def __str__(self):
            return self.name



