from django.urls import path
from .views import wallet_transfer
urlpatterns = [
    path("transfer/", wallet_transfer, name="transfer"),
]