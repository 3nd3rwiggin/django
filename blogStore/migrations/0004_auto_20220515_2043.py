# Generated by Django 2.2.26 on 2022-05-15 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogStore', '0003_auto_20220514_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likesCount',
        ),
        migrations.RemoveField(
            model_name='post',
            name='viewCount',
        ),
    ]