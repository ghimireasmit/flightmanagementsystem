from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserSignupForm
from .models import User
from django.contrib import messages


def usersignup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            user_email = form.cleaned_data['userEmail']
            user_password = form.cleaned_data['userPassword']
            user_first_name = form.cleaned_data['userFname']
            user_last_name = form.cleaned_data['userLname']
            user_dob = form.cleaned_data['userDob']
            user_phone = form.cleaned_data['userPhone']
            
            # Create a new user instance
            user = User.objects.create_user(
                email=user_email,
                password=user_password,
                first_name=user_first_name,
                last_name=user_last_name,
                date_of_birth=user_dob,
                phone=user_phone
            )
            # Authenticate the user
            user = authenticate(request, email=user_email, password=user_password)
            if user is not None:
                # Log the user in after signup
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                # Redirect to user's homepage
                return redirect('userhomepage')
            else:
                # Handle authentication failure
                messages.error(request, 'Failed to authenticate user after signup.')
    else:
        form = UserSignupForm()
    
    return render(request, 'user/usersignup.html', {'form': form})


def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to user's homepage
            return redirect('userhomepage')
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid email or password. Please try again.')
    return render(request, 'user/userlogin.html')


def userhomepage(request):
    if request.user.is_authenticated:
        return render(request, 'user/userhomepage.html')
    else:
        return redirect('userlogin')


def index(request):
    return render(request, "index.html")


def flightbooking(request):
    return render(request, "flightbooking.html")


def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

def airlinelogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to user's homepage
            return redirect('flightbooking.html')
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid email or password. Please try again.')
    return render(request, 'airline/airlinelogin.html')


def adminlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to user's homepage
            return redirect('adminhomepage.html')
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid email or password. Please try again.')
    return render(request, 'admin/adminlogin.html')