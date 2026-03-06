from django.urls import path
from .views import create_wallet_account, login

urlpatterns = [
    path("register/", create_wallet_account, name="register"),
    path("login/", login, name="login")
]