from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import Company

@receiver(post_save, sender=Company)
def company_created_or_updated(sender, instance, created, **kwargs):
    if created:
        print(f"New company created: {instance.name}")
    else:
        print(f"Company updated: {instance.name}")

@receiver(post_delete, sender=Company)
def company_deleted(sender, instance, **kwargs):
    print(f"Company deleted: {instance.name}")