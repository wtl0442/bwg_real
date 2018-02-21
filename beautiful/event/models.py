from django.db import models
from django.urls import reverse
from django.conf import settings
from django_google_maps import fields as map_fields

# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.tag_name


class Event(models.Model):
    title = models.CharField(max_length=30, verbose_name='행사 이름')
    place = models.CharField(max_length=30, verbose_name='행사 장소')
    date = models.DateField(verbose_name='행사 날짜')
    time = models.TimeField(verbose_name='행사 시간')
    content = models.TextField(verbose_name='행사 설명')
    tag2 = models.CharField(max_length=10, default=None, blank=True, null=True, verbose_name='행사 성격 태그')
    tag = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='태그')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event:event_main')



# Create your models here.

class Googlemap(models.Model):
    place_name = models.CharField(max_length=30, verbose_name='장소 이름')
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.place_name
