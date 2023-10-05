from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Use RegexValidator to ensure phonenumber is exactly 10 digits and contains only numbers
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits and contain only numbers.",
    )
    phonenumber = models.CharField(validators=[phone_regex], max_length=10)
    message_text = models.TextField()

    def __str__(self):
        return self.name



class Booking(models.Model):
    fullname = models.CharField(max_length=255)
    petname = models.CharField(max_length=255)
    email = models.EmailField()
    
    # Use RegexValidator to ensure phonenumber is exactly 10 digits and contains only numbers
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits and contain only numbers.",
    )
    phonenumber = models.CharField(validators=[phone_regex], max_length=10)
    
    booking_date = models.DateField()
    booking_time = models.TimeField()
    # Add more fields as needed

    def __str__(self):
        return f'Booking for {self.petname} on {self.booking_date} at {self.booking_time}'
    
class Hostelbooking(models.Model):
    fullname = models.CharField(max_length=255)
    petname = models.CharField(max_length=255)
    email = models.EmailField()
     # Use RegexValidator to ensure phonenumber is exactly 10 digits and contains only numbers
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits and contain only numbers.",
    )
    phonenumber = models.CharField(validators=[phone_regex], max_length=10)
    booking_from= models.DateField()
    booking_to = models.DateField()
    # Add more fields as needed

    def __str__(self):
        return f'Booking for {self.petname} on {self.booking_from} '
