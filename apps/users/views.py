from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {user_name}, your account is created!')
            return redirect('food:index')
    else:
        form = UserCreationForm()        

    return render(request, 'users/register.html', {'form': form})
