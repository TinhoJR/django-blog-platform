from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from core.communication import CustomEmail
from django.db import transaction

User = get_user_model()

@receiver(post_save,sender=User)
def handle_registered_user(sender,instance,created,**kwargs):


    if created:
        mail = CustomEmail(instance,"support")
        transaction.on_commit(mail.send_registration_email)
        # mail.send_registration_email()
        # instance.profile.create()









