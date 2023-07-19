from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import AddProfileForm

def user_login(request):
    if request.user.is_authenticated:
         return redirect('account:dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Invalid Username or Password')
    return render(request, 'login.html')


@login_required(login_url='/')
def logout_user(request):
	logout(request)
	return redirect("account:login")

@login_required(login_url='/')
def dashboard(request):
    profiles = Profile.objects.all()

    context = {'profiles':profiles}
    return render(request, 'dashboard.html', context)


def search_result(request, slug):
     profile = Profile.objects.get(slug=slug)
     
     context = {'profile':profile}
     return render(request, 'search_result.html', context)


def add_new_profile(request):
    form = AddProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
         form.save()
         messages.success(request, 'The profile was added successfully')
         return redirect('account:add_new_profile')

    context = {'form': form}
    return render(request, 'add_profile.html', context)


def delete_profile(request, slug):
    profile = Profile.objects.get(slug=slug)
    profile.delete()
    messages.success(request, 'Profile was deleted successfully!')
    return redirect('account:dashboard')


def edit_profile(request, slug):
    profile = Profile.objects.get(slug=slug)
    form = AddProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
         form.save()
         messages.success(request, 'The profile was edited successfully')
         return redirect('account:dashboard')

    context = {'form': form}
    return render(request, 'edit_profile.html', context)
