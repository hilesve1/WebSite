# Generated by Django 3.1.7 on 2021-04-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210318_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pic',
            field=models.ImageField(upload_to='user_images', verbose_name='Добавить фото'),
        ),
    ]
