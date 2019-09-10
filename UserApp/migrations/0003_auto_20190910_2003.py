# Generated by Django 2.0.1 on 2019-09-10 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0004_auto_20190910_1954'),
        ('UserApp', '0002_auto_20190910_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='navmodel',
            name='actives_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Navs', to='Address.ActivesModel', verbose_name='活动ID'),
        ),
        migrations.AlterField(
            model_name='navmodel',
            name='nav_child_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nav', to='Funy.CategoryModel', verbose_name='分类ID'),
        ),
    ]
