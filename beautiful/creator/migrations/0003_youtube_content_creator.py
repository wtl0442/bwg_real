# Generated by Django 2.0.1 on 2018-02-03 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creator', '0002_auto_20180130_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube_content',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
