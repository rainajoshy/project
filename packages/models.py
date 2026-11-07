from django.db import models

class Package(models.Model):
    package_name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.package_name
