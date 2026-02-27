from .models import Notification
from django.core.mail import send_mail


def create_notification(user):
    notification = Notification.objects.create(
        user=user,
        message=f"""Hi {user.first_name} Welcome to MAXL WALLET
        Your wallet number is: {user.wallet.wallet_number}
        Your alternate wallet number is: {user.wallet.account_number}

"""
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