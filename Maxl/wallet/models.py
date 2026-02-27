import uuid

from django.db import models
from .util import generate_account_number, generate_reference_number
from django.conf import settings

# Create your models here.
class Wallet(models.Model):

    CURRENCY_CHOICES = (
        ('NGN', 'Naira'),
        ('USD', 'Dollar'),
        ('EUR', 'Euro'),

    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    wallet_number = models.CharField(max_length=10, unique=True)
    account_number = models.CharField(max_length=10, unique=True, default= generate_account_number)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='NGN')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    )

    TRANSACTION_STATUS = (
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    )

    reference = models.CharField(max_length=10, unique=True, default= generate_reference_number())
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sender = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='sender')
    receiver = models.ForeignKey(Wallet, on_delete=models.PROTECT, related_name='receiver')
    status = models.CharField(max_length=7, choices=TRANSACTION_STATUS)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    idempotency_key = models.UUIDField(unique="True", editable=False, blank=True, null=True)


class Ledger(models.Model):
    TRANSACTION_TYPE = (
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    )

    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    balance_after = models.DecimalField(max_digits=10, decimal_places=2)
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    entry_type = models.CharField(max_length=6, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)



