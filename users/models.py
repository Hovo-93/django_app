from django.core.validators import EmailValidator
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField([EmailValidator(message='Enter a valid email address.')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
