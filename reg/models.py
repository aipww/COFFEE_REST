from django.db import models
from django.conf import settings


class UserReg(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    pas = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)