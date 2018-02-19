from django.db import models
from creator.models import Item


class TroubleWiki(models.Model):
    name = models.CharField(max_length=20)
    contents = models.TextField()
    solution = models.TextField(blank=True, null=True)
    item = models.ManyToManyField(Item, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="wiki")

    def __str__(self):
        return self.name

    def image_url(self):
        if self.image:
            image_url = self.image.url
        else:
            image_url = '/static/img/wiki/no_image.png'
        return image_url


