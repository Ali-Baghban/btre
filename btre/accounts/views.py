from django.shortcuts import render, redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User
def checkpoint(request):
    return render(request, 'accounts/checkpoint.html')

def login(request):
    # Login User
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Welcome dear '+username)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials ')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    # Registration User
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if len(password) | len(repassword) < 8 :
            messages.error(request, 'Your password is short, it must be greater than 8 characters !')
            return redirect('register')
        else:
            if password != repassword : 
                messages.error(request, 'Password does not match !')
                return redirect('register')
            else:
                if  User.objects.filter(username=username).exists():
                    messages.error(request, 'The username is token !')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'The email has registered before !')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(
                            username=username, password=password, email=email, first_name=first_name,
                            last_name=last_name
                        )
                        user.save()
                        messages.success(request, 'Congratulation, you are successfully registered !')
                        return redirect('login')
                        
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    return redirect ('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
