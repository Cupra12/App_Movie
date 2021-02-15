from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm




def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto utworzone dla "{username}" !') # wiadomość dla usera i sukcesie zalłożenia konta
            return redirect('MyWebsiteUsers:login')
    else:
        form = UserRegisterForm()
    return render(request, 'My_Website_User/Register.html', {'form': form})

