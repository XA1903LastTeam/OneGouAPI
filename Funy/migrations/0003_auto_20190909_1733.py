# Generated by Django 2.0.1 on 2019-09-09 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Funy', '0002_auto_20190909_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='father_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Funy.CategoryModel', verbose_name='父分类名'),
        ),
    ]
