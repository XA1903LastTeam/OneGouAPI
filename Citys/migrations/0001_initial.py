# Generated by Django 2.0.1 on 2019-09-09 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityAreaModels',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityareaname', models.CharField(max_length=50, verbose_name='区域名称')),
            ],
            options={
                'verbose_name': '区域',
                'verbose_name_plural': '区域',
                'db_table': 't_city_area',
            },
        ),
        migrations.CreateModel(
            name='CityModels',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=10, verbose_name='城市名称')),
                ('city_letter', models.CharField(max_length=10, verbose_name='首字母名称')),
                ('city_hot', models.IntegerField(verbose_name='热度')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
                'db_table': 't_city',
            },
        ),
        migrations.AddField(
            model_name='cityareamodels',
            name='city_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='citys', to='Citys.CityModels', verbose_name='所属城市'),
        ),
    ]
