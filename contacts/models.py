from django.db import models
from datetime import datetime

class Contacts(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    companyName = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    county = models.CharField(max_length=32)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    phone1 = models.CharField(max_length=12)
    phone2 = models.CharField(max_length=12)
    email = models.CharField(max_length=45)
    website = models.CharField(max_length=45)
    created = models.DateTimeField(default=datetime.now, blank=True)
    modified = models.DateTimeField(default=datetime.now, blank=True)

    # define presentation in admin list view
    def __str__(self):
        return f"{self.firstName} {self.lastName} ({self.state})"

    # A consequence of using a plural model name - we have to inhibit default pluralization
    class Meta:
        verbose_name_plural = "Contacts"

