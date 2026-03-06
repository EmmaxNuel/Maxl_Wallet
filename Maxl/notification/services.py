from wallet.models import Wallet
from .models import Notification
from django.core.mail import send_mail


def create_notification(user):
    notification = Notification.objects.create(
        wallet=user.wallet.wallet_number,
        user=user,
        message=f"""Hi {user.first_name} Welcome to MAXL WALLET
        Your wallet number is: {user.wallet.wallet_number}
        Your alternate wallet number is: {user.wallet.account_number}

""",
    event_type = 'USER_WALLET_CREATED',
    )

    send_mail(
        subject = "Welcome to MAXL WALLET",
        message = notification.message,
        from_email='',
        recipient_list = [user.email],
        fail_silently= True
    )

    notification.is_read = True
    notification.save()