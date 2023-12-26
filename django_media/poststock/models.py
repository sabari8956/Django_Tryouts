from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from azure.storage.blob import generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

def user_profile_image_upload_to(instance, filename):
    return f'profiles/{instance.username}/{filename}'

class User(AbstractUser):
    profile_img = models.ImageField(upload_to=user_profile_image_upload_to, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.username}"

    def get_profile_img_url(self):
        # Generate a SAS token for the blob
        sas_token = generate_blob_sas(
            account_name=settings.AZURE_ACCOUNT_NAME,
            container_name=settings.AZURE_CONTAINER,
            blob_name=self.profile_img.name,
            account_key=settings.AZURE_ACCOUNT_KEY,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(seconds=30)  # Adjust the expiry as needed
        )

        # Construct the complete URL with SAS token
        base_url = f'https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net/{settings.AZURE_CONTAINER}/{self.profile_img.name}?{sas_token}'
        return base_url
