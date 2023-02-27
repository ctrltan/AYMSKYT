from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ..forms import *
from ..models import *
from django.contrib import messages
from ..decorators import login_prohibited
from .views_functions.login_view_functions import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

@login_prohibited
def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            user = get_user(form)
            if user:
                user.last_login
                login(request, user)
                check_streak(user)
                redirect_url = request.POST.get('next') or get_redirect_url_for_user(user)
                return redirect(redirect_url)
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    next_url = request.GET.get('next') or request.POST.get('next') or ''
    return render(request, 'login.html', {'form': form, 'next': next_url})
    
def check_streak(user):
    if (user.streak_data.last_login_time == None):
        user.streak_data.last_login_time = user.last_login
        user.streak_data.streak = user.streak_data.streak + 1
        print("hi")
    else:
        print("poo")
    
        
        
    

def log_out(request):
    logout(request)
    return redirect('home')

@login_prohibited
def home(request):
    return render(request, 'homepage.html')

@login_prohibited
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    return render(request,'dashboard.html')


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details were successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditProfileForm(instance= request.user)
    return render(request, 'edit_profile.html', {'form': form})
    
@login_required
def change_password(request):
    current_user = request.user
    if request.method == 'POST':
        form = PasswordForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            if check_password(password, current_user.password):
                new_password = form.cleaned_data.get('new_password')
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(request, current_user)
                messages.add_message(request, messages.SUCCESS, "Password updated!")
                return redirect('profile')
    form = PasswordForm()
    return render(request, 'change_password.html', {'form': form})

    
    

