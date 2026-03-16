from django.urls import path

from wallet.views import dashboard, wallet_transfer

urlpatterns = [
    path("transfer/", wallet_transfer, name="transfer"),
    path("dashboard/", dashboard, name="dashboard"),
]