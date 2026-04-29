from django.db import models
class Company(models.Model):
    TYPE_CHOICES = (
        ('software', 'Software'),
        ('ai', 'AI'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('telecom', 'Telecommunication'),
        ('retail', 'Retail'),
        ('other', 'Other'),
    )
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices= TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)  # set once
    updated_at = models.DateTimeField(auto_now=True)  # updates each save
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name +' '+ self.location
