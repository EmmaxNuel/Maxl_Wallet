from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Wallet
from .serializers import WalletTransferSerializer
from wallet.services.intra_transfer import transfer_wallet_to_wallet
from django.shortcuts import render, get_object_or_404


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def wallet_transfer(request):
    sender = request.user.wallet
    serializer = WalletTransferSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    description = serializer.validated_data['description']
    receiver_wallet = serializer.validated_data['receiver_wallet']

    amount = serializer.validated_data['amount']
    idempotency_key = serializer.validated_data['idempotency_key']
    receiver = get_object_or_404(Wallet, wallet_number=receiver_wallet.pk)
    tx = transfer_wallet_to_wallet(sender, receiver,amount, idempotency_key,description)

    return Response(
        {
            "reference": tx.reference,
            "amount": tx.amount,
            "status": tx.status,
            "description": tx.description,
            "created_at": tx.created_at,
        },
        status = status.HTTP_201_CREATED
    )

