from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app1.models import PetInsurance
from .forms import BookingForm
from .forms import HostelForm
from .forms import ContactForm
from django.contrib import messages

import re

# Create your views here.

def servicepage(request):
     return render (request,'services.html')
    
def Homepage(request):
    return render (request,'landing.html')  

@csrf_protect


def about(request):
    return render (request,'about.html')

def insurance(request):
    return render (request,'insurance.html')


@login_required(login_url='login')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Messages is Send.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the phone number.')
    else:
        form = ContactForm()
    return render (request,'contact.html', {'form': form})  

def Hostelbooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking successfully created.')
            return redirect('services')
        else:
            messages.error(request, 'Please correct the phone number.')
    else:
        form = BookingForm()

    return render(request, 'services.html', {'form': form})

def Appointement(request):
    if request.method == 'POST':
        form = HostelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment successfully created.')
            return redirect('appointment')  # Redirect to the next page
        else:
            messages.error(request, 'Please correct the phone number.')

    else:
        form = HostelForm()

    return render(request, 'services.html', {'form': form})


def Booking(request):
    return render(request, 'booking.html')

def Insurance(request):
    return render(request, 'insurance.html')

def Hostelfacilities(request):
    return render(request, 'hostel.html')

def Food(request):
    return render(request, 'food.html')

def Book(request):
    return render(request, 'book.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')


def Registerpage(request):
    def is_strong_password(password):
        # Check for at least 8 characters
        if len(password) < 8:
            return False

        # Check for at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False

        # Check for at least one lowercase letter
        if not any(char.islower() for char in password):
            return False

        # Check for at least one digit
        if not any(char.isdigit() for char in password):
            return False

        # Check for the presence of a special character (symbol)
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False

        return True

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        elif not is_strong_password(pass1):
            return HttpResponse("Your password does not meet the strength criteria. It should include a combination of uppercase letters, lowercase letters, numbers, and symbols.")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'register.html')


def payment(request):
    return render(request, 'payment.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')
    



# views.py
from django.shortcuts import render, redirect
from .forms import PetInsuranceForm


from django.http import JsonResponse

# def process_payment(request):
#     if request.method == 'POST' and request.is_ajax():
#         pet_name = request.POST.get('petName')
#         owner_name = request.POST.get('ownerName')
#         insurance_name = request.POST.get('insuranceName')
#         start_date = request.POST.get('startDate')
        
#         # Create a new PetInsurance object and save it to the database
#         pet_insurance = PetInsurance(pet_name=pet_name, owner_name=owner_name, insurance_name=insurance_name, start_date=start_date)
#         pet_insurance.save()
        
#         return JsonResponse({'status': 'success'})

#     return JsonResponse({'status': 'error'})

from django.http import JsonResponse


def process_payment(request):
    if request.method == 'POST':
        form = PetInsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            print(form.errors)
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})

# def process_payment(request):
#     if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         pet_name = request.POST.get('petName')
#         owner_name = request.POST.get('ownerName')
#         insurance_name = request.POST.get('insuranceName')
#         start_date = request.POST.get('startDate')

#         # Create a new PetInsurance object and save it to the database
#         pet_insurance = PetInsurance(pet_name=pet_name, owner_name=owner_name, insurance_name=insurance_name, start_date=start_date)
#         pet_insurance.save()

#         return JsonResponse({'status': 'success'})

#     return JsonResponse({'status': 'error'})

# def process_payment(request):
#     print(request.POST)  # Add this line for debugging
