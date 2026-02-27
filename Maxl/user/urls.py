from django.urls import path
from .views import create_wallet_account

urlpatterns = [
    path("register/", create_wallet_account, name="register")
]