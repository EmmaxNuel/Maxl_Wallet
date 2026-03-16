from rest_framework import serializers

from wallet.models import Wallet


class WalletTransferSerializer(serializers.Serializer):
    receiver_wallet = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    idempotency_key = serializers.UUIDField()
    description = serializers.CharField(max_length=100,required=False)

    def validate_amount(self,amount):
        if amount < 0:
            raise Exception("Amount cannot be negative 😉😉😉😉😉")
        return amount

    def validate_receiver_wallet(self,value):
        try:
            receiver_wallet = Wallet.objects.get(wallet_number=value)
        except:
            raise Exception("Wallet does not exist")

        return receiver_wallet