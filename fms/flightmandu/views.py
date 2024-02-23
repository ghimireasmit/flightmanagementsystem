from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .forms import UserSignupForm
from .models import User, ContactMessage
from django.contrib import messages


def usersignup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['userEmail']
            first_name = form.cleaned_data['userFname']
            last_name = form.cleaned_data['userLname']
            date_of_birth = form.cleaned_data['userDob']
            phone = form.cleaned_data['userPhone']
            password = form.cleaned_data['userPassword']
            
            if User.objects.filter(email=email).exists():
                form.add_error('userEmail', 'Email is already in use.')
                return render(request, 'user/usersignup.html', {'form': form})
            
            if User.objects.filter(phone=phone).exists():
                form.add_error('userPhone', 'Phone number is already in use.')
                return render(request, 'user/usersignup.html', {'form': form})

            new_user = User(email=email, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, phone=phone)
            new_user.set_password(password)
            new_user.save()
            
            return redirect('success_page')
    else:
        form = UserSignupForm()
    return render(request, 'user/usersignup.html', {'form': form})

def check_email_availability(request):
    email = request.POST.get('email')
    if User.objects.filter(email=email).exists():
        return JsonResponse({'available': False})
    return JsonResponse({'available': True})

def check_phone_availability(request):
    phone = request.POST.get('phone')
    if User.objects.filter(phone=phone).exists():
        return JsonResponse({'available': False})
    return JsonResponse({'available': True})


def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other page you want
            return redirect('userhomepage')
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid email or password. Please try again.')
            return redirect('userlogin')  # Adjust this to your login page URL
    else:
        return render(request, 'user/userlogin.html')  # Adjust this to your login page template path



def userhomepage(request):
    return render(request, 'user/userhomepage.html')


def index(request):
    return render(request, "index.html")

def flightbooking(request):
    return render(request, "flightbooking.html")

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(index)



def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create and save the ContactMessage object
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return render(request, 'index.html')

    return render(request, 'index.html')