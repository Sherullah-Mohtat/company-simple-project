from django.db import models
class Employee(models.Model):

    POSITION_CHOICES = (
        ('Manager', 'Manager'),
        ('Software Developer', 'Software Developer'),
        ('Project Leader', 'Project Leader'),
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.name