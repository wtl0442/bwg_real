from django.db import models
from creator.models import Item

# Create your models here.


class review(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')
    rev_date = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    Item = models.ForeignKey(
            Item,
            on_delete=models.CASCADE,
            verbose_name='해당 제품',
            related_name='review'
    )

    def __str__(self):
        return '{0}, {1}'.format(self.pk ,self.title)


# 작성자 추가 시켜야함

