from django.db import models
from django.conf import settings
# Create your models here.


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


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='상품명')
    image = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")
    description = models.TextField(verbose_name='상품 설명')

    def __str__(self):
        return '{0}, {1}'.format(self.pk ,self.name)


# class Review(models.Model):
#     title = models.CharField(max_length=200, verbose_name='제목')
#     content = models.TextField(verbose_name='내용')
#     item = models.ForeignKey(
#         Item,
#         on_delete=models.CASCADE)
#     # user =

#     def __str__(self):
#         return '{0}, {1}'.format(self.item.name, self.content)

