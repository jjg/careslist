from django.db import models
from django.utils import timezone

class Business(models.Model):
    name = models.CharField("business name",max_length=200)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    created_datetime = models.DateTimeField(default=timezone.now)
    verified_date = models.DateField("date verified",null=True)

    def __str__(self):
        return self.name

    def verified(self):
        if self.verified_date:
            return self.verified_date
        else:
            return False
