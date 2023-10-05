from django.forms import ModelForm
from .models import Contact
from .models import Booking
from .models import Hostelbooking
from django import forms
from django.core.validators import RegexValidator




class BookingForm(forms.ModelForm):
    # Define a RegexValidator for the phone number
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits and contain only numbers.",
    )

    # Use the RegexValidator for the phonenumber field
    phonenumber = forms.CharField(validators=[phone_regex])

    class Meta:
        model = Booking
        fields = ['fullname', 'petname', 'email', 'phonenumber', 'booking_date','booking_time']



class HostelForm(forms.ModelForm):
    # Define a RegexValidator for the phone number
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits and contain only numbers.",
    )

    # Use the RegexValidator for the phonenumber field
    phonenumber = forms.CharField(validators=[phone_regex])

    class Meta:
        model = Hostelbooking
        fields = ['fullname','petname','email','phonenumber','booking_from','booking_to']
        


class ContactForm(ModelForm):
     # Define a RegexValidator for the phone number
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits and contain only numbers.",
    )

    # Use the RegexValidator for the phonenumber field
    phonenumber = forms.CharField(validators=[phone_regex])
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phonenumber', 'message_text']