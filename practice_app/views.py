from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.


def index(request):
    return render(request, 'index.html')


def reg(request):
    errors = Users.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
        # to not duplicate emails or users with above code in order to keep an account per user in db
    is_user_in_db = Users.objects.filter(email=request.POST['email']).first()
    if is_user_in_db:
        print("User already exists")
        return redirect("/")
    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()

    new_user = Users.objects.create(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        password=hashed_pw,
    )

    request.session['user_id'] = new_user.id

    return redirect('/success')


def success(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        messages.error(request, 'Try to login/register')
        return redirect('/')
    else:
        user_from_db = Users.objects.get(id=user_id)
        context = {
            "user": user_from_db
        }
        return render(request, 'success.html', context)


def login(request):
    found_user = Users.objects.filter(email=request.POST['email'])
    print("%"*100)
    print(found_user)
    if found_user:  # if user is found , below code will unhash passwords to compare them
        is_pw_correct = bcrypt.checkpw(
            # sends pass from form and user to compare them
            request.POST['password'].encode(),
            found_user.password.encode()
        )
        if is_pw_correct:
            request.session['user_id'] = found_user.id
            return redirect('/success')
        else:
            print("Incorrect Password")
            return redirect("/")
    else:
        print("No User Found")
        return redirect("/")

    messages.error(request, 'Invalid Credintials')
    return redirect('/')


def logout(request):
    request.session.clear
    return redirect('/')

# print('Logging in user')
# return redirect('/dashboard')

# print(request.POST)
# print('Registered user')
# request.session['user_id'] = request.POST['email']
# return redirect('/dashboard')


# def dashboard(request):
#     print('renedering the dashboard')
#     return render(request, 'dashboard.html')
