from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, "index.html")

def adminlogin(request):
    if request.user.is_authenticated:
        return redirect('adminhomepage')  # Redirect to admin home if already authenticated
    
    if request.method == 'POST':
        userEmail = request.POST.get('email')  # Fix this to match your input name in the form
        userPassword = request.POST.get('password')  # Fix this to match your input name in the form

        user = authenticate(username=userEmail, password=userPassword)

        if user is not None:
            login(request, user)
            return redirect('adminhomepage')  # Redirect to admin home upon successful login
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect('adminlogin')  # Redirect back to login page if authentication fails

    return render(request, "admin/adminlogin.html")

def adminhomepage(request):
    return render(request, "admin/adminhomepage.html")

def airlinelogin(request):
    error_message = None
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if email and password are provided
        if email and password:
            # Authenticate user
            user = authenticate(username=email, password=password)
            if user is not None:
                # Check if the user is active
                if user.is_active:
                    # Log the user in
                    login(request, user)
                    # Redirect to a success page or do something else
                    return redirect("adminhomepage")
                else:
                    # Set an error message if the account is not active
                    error_message = "Your account is not active."
            else:
                # Set an error message if authentication fails
                error_message = "Invalid email or password."
        else:
            # Set an error message if email or password is not provided
            error_message = "Email and password are required."
    
    # Render the login form with error message for GET requests
    return render(request, "airline/airlinelogin.html", {'error_message': error_message})


def usersignup(request):
    if request.method == "POST":
        userFname = request.POST.get('userFname')
        userLname = request.POST.get('userLname')
        userDob = request.POST.get('userDob')
        userEmail = request.POST.get('userEmail')
        userPhone = request.POST.get('userPhone')
        userPassword = request.POST.get('userPassword')
        userCpassword = request.POST.get('userCpassword')

        myuser = User.objects.create_user(username=userEmail, email=userEmail, password=userPassword)
        myuser.first_name = userFname
        myuser.last_name = userLname
        myuser.phone = userPhone
        myuser.dob = userDob
        myuser.save()

        # Check if the user is saved in the backend
        user_exists = User.objects.filter(email=userEmail).exists()
        if user_exists:
            messages.success(request, "Your account has been successfully created.")
        else:
            messages.error(request, "There was an issue creating your account. Please try again.")

        return redirect('userlogin')

    return render(request, "usersignup.html")

def userlogin(request):
    if request.method == 'POST':
        userEmail = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')

        user = authenticate(username=userEmail, password=userPassword)
    return render(request, "userlogin.html")


def signout(request):
    # You need to implement signout functionality here
    pass
