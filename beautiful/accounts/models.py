from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class SkinType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    birth_date = models.DateField(null=True, blank=True)
    skin_type = models.ForeignKey(SkinType, on_delete=models.CASCADE, verbose_name='피부타입', related_name='profile', blank=True, null=True)
    image = models.ImageField(
        upload_to='profile/%Y/%m/%d/',
        blank=True,
    )
    is_creator = models.BooleanField(default=False)
    creator_header_img = models.ImageField(
        upload_to='creator/%Y/%m/%d/',
        blank=True,
        null=True,
    )

    def image_url(self):
        if self.image:
            image_url = self.image.url
        else:
            image_url = '/static/img/default_image.png'
        return image_url

    def creator_header_image_url(self):
        if self.creator_header_img:
            image_url = self.creator_header_img.url
        else:
            image_url = '/static/header-ex.jpg'
        return image_url

    def __str__(self):
        return self.user.username


