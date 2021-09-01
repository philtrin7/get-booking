from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=10, blank=False)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
