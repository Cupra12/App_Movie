from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm, ProfilePageForm,PasswordChangingForm
from django.views import generic
from django .contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .models import Profile



def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto utworzone dla "{username}" !')
            return redirect('MyWebsiteUsers:login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/Register.html', {'form': form})



class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/Edit_profile.html'
    success_url = reverse_lazy('Home')

    def get_object(self):
        return self.request.user



class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangingForm
    template_name = 'registration/Change_Password.html'
    success_url = reverse_lazy('password_success')



def PasswordSuccess(request):
    return render(request, 'registration/Password_Success.html', {})



class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/User_Profile.html'
    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all(),
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context



class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/Edit_profile_page.html'
    fields = ['my_photo', 'website_url']
    success_url = reverse_lazy('Home')



class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/Create_User_Profile.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)