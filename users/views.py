from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Your Account has been Created')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def profile(request):
    return render(request,'profile.html')