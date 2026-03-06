from django.db import models
from django.conf import settings
# Create your models here.

class Notification(models.Model):
    CHANNEL_TYPE = (
        ('EMAIL', 'Email'),
        ('SMS', 'sms')
    )

    wallet = models.CharField(max_length=10, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    reference = models.CharField(max_length=40, unique=True, blank=True, null=True)
    message = models.TextField(blank=True)
    channel = models.CharField(max_length=10, choices=CHANNEL_TYPE,default='EMAIL')
    created_at = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)

