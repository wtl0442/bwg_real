from django.db import models
from django.conf import settings
# Create your models here.

from accounts.models import SkinType


class Youtube_Content(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Youtube_Content',
    )
    title = models.CharField(max_length=50, verbose_name='제목')
    description = models.TextField(verbose_name='설명')
    youtube_url = models.URLField(verbose_name='링크')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')
    item = models.ManyToManyField('Item', blank=True, null=True, verbose_name='제품')

    def get_URL(self):
        return self.youtube_url

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='브랜드명')

    def __str__(self):
        return '{0}'.format(self.name)


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='상품명')
    item_image = models.ImageField(blank=True, upload_to="item/%Y/%m/%d")
    description = models.TextField(verbose_name='상품 설명')
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(
                Brand,
                on_delete=models.CASCADE,
                verbose_name='브랜드명',
                related_name='brand_item',
                blank=True,
                null=True)
    skin_type = models.ForeignKey(
                SkinType,
                on_delete=models.CASCADE,
                verbose_name='skin_type_item',
                blank=True,
                null=True
                )

    def item_image_url(self):
        if self.item_image:
            image_url = self.item_image.url
        else:
            image_url = '/static/no-image.jpg'
        return image_url

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.pk, self.brand.name, self.name)


class Review(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author_review'
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')
    rev_date = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    Item = models.ForeignKey(
            Item,
            on_delete=models.CASCADE,
            verbose_name='해당 제품',
            related_name='item_review'
    )

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.pk, self.title, self.Item.name)