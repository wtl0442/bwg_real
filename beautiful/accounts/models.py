from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    birth_date = models.DateField(null=True, blank=True)
    skin_type = models.CharField(max_length=30, blank=True)
    image = models.ImageField(
        upload_to='profile/%Y/%m/%d/',
        blank=True,
    )
    is_creator = models.BooleanField(default=False)

    def image_url(self):
        if self.image:
            image_url = self.image.url
        else:
            image_url = '/static/img/default_image.png'
        return image_url


    def __str__(self):
        return self.user.username
