# Generated by Django 2.0.1 on 2019-09-12 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.CharField(default='photo/photo.jpg', max_length=200, verbose_name='用户头像'),
        ),
    ]