from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import UserCreateView, email_verification, reset_password

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path('password-reset/', reset_password, name='password_reset'),
]
