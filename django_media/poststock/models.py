from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
def user_profile_image_upload_to(instance, filename):
    print(instance)
    return f'profiles/{instance.username}/{filename}'

class User(AbstractUser):
    profile_img = models.ImageField(upload_to=user_profile_image_upload_to, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.username}"