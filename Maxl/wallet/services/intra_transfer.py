from decimal import Decimal
from uuid import UUID
from django.db import transaction
from wallet.models import Wallet, Transaction, Ledger


def transfer_wallet_to_wallet(sender: Wallet, receiver: Wallet, amount: Decimal, idempotency_key: UUID, description: str):
    if sender.pk == receiver.pk:
        raise Exception("Cannot transfer to self")

    if amount > sender.balance:
        raise Exception("Insufficient balance")

    existing_tx = Transaction.objects.filter(idempotency_key=idempotency_key).first()
    if existing_tx:
        return existing_tx

    with transaction.atomic():
        receiver_wallet = Wallet.objects.select_for_update().get(pk=receiver.pk)
        sender_wallet = Wallet.objects.select_for_update().get(pk=sender.pk)

        sender_wallet.balance -= amount
        receiver_wallet.balance += amount
    sender_wallet.save(update_fields=["balance"])
    receiver_wallet.save(update_fields=["balance"])


    tx = Transaction.objects.create(
        sender=sender,
        receiver=receiver,
        amount=amount,
        idempotency_key=idempotency_key,
        description=description,
        status='SUCCESS',
        transaction_type='CREDIT'
    )


    Ledger.objects.create(
        transaction=tx,
        amount=amount,
        wallet=receiver_wallet,
        balance_after=receiver.balance,
        entry_type='CREDIT',

    )

    Ledger.objects.create(
        transaction=tx,
        amount=amount,
        wallet=sender_wallet,
        balance_after=sender.balance,
        entry_type='DEBIT',
    )



    return tx
