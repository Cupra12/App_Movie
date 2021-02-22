from django.urls import path
from . views import UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy
from . import views as user_views



app_name = 'MyWebsiteUsers'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', user_views.Register, name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(success_url=reverse_lazy('MyWebsiteUsers:password_success')), name='Change_Password'),
    path('password_success/', views.PasswordSuccess, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),

]