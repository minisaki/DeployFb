# Generated by Django 3.2.8 on 2021-10-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20211010_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfacebook',
            name='file',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image', verbose_name='post'),
        ),
    ]
