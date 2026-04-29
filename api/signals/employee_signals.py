from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import Employee

@receiver(post_save, sender=Employee)
def employee_created_or_updated(sender, instance, created, **kwargs):
    if created:
        print(f"New employee created: {instance.name}")
    else:
        print(f"Employee updated: {instance.name}")

@receiver(post_delete, sender=Employee)
def employee_deleted(sender, instance, **kwargs):
    print(f"Employee deleted: {instance.name}")