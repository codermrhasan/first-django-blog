from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm
)

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been successfully created! Try to Log In now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    template_name = 'account/signup.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
         u_form = UserUpdateForm(instance=request.user)
         p_form = ProfileUpdateForm(instance=request.user.profile)
    
    template_name = 'account/profile.html'
    context = { 
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, template_name, context)

@login_required
def delete_account(request):
    userobject = get_object_or_404(User, id=request.user.id)
    template_name = 'account/delete.html'
    if request.method == 'POST':
        userobject.delete()
        messages.success(request, f'Your account has been deleted. We are sorry to see you gone.')
        return redirect('home')
    return render(request, template_name)