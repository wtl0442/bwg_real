# Generated by Django 2.0.1 on 2018-02-10 11:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_subscribedemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribedemail',
            name='subscribe_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]