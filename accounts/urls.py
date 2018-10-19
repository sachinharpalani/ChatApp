from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import register, logout

app_name='accounts'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout')
    ]
