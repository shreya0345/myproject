# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    # Print the current thread
    print(f'Signal handler executed in thread: {threading.current_thread().name}')


