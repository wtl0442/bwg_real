from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Post(models.Model):
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    hashtag = models.CharField(max_length=10)
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    file = models.FileField(blank=True)
    photo = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.content

# class UploadFile(models.Model):
#     title = models.TextField(default='')
#     file = models.FileField(null=True)
