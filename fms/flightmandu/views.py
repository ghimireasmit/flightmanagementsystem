from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def index(request):
    return render(request, "index.html")

def adminlogin(request):
    if request.user.is_authenticated:
        return redirect('adminhome')  # Redirect to admin home if already authenticated
    
    if request.method == 'POST':
        userEmail = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')

        user = authenticate(username=userEmail, password=userPassword)

        if user is not None:
            login(request, user)
            return redirect('adminhome')  # Redirect to admin home upon successful login
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect('adminlogin')  # Redirect back to login page if authentication fails

    return render(request, "admin/adminlogin.html")



def adminhome(request):
    return render(request, "admin/adminhome.html")

def signup(request):
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

        return redirect('signin')

    return render(request, "signup.html")

def signin(request):
    if request.method == 'POST':
        userEmail = request.POST.get('userEmail')
        userPassword = request.POST.get('userPassword')

        user = authenticate(username=userEmail, password=userPassword)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, f"Welcome back, {fname}!")
            return redirect('index')  # Assuming 'index' is the appropriate landing page
        else:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect('home')  # Redirect to 'home' if authentication fails

    return render(request, "signin.html")

def signout(request):
    # You need to implement signout functionality here
    pass
