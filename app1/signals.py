from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tenant, members



def save_profile(sender, instance, **kwargs):
    print('hello world!!!')

post_save.connect(save_profile, sender=members)