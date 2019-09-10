# Generated by Django 2.0.1 on 2019-09-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivesModel',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_name', models.CharField(max_length=100, verbose_name='活动名称')),
                ('active_url', models.CharField(max_length=100, verbose_name='活动跳转链接')),
                ('icon', models.CharField(max_length=100, verbose_name='活动缩略图')),
            ],
            options={
                'verbose_name': '活动表',
                'verbose_name_plural': '活动表',
                'db_table': 't_adtives',
            },
        ),
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='用户地址')),
            ],
            options={
                'verbose_name': '用户地址表',
                'verbose_name_plural': '用户地址表',
                'db_table': 't_address',
            },
        ),
        migrations.CreateModel(
            name='DiscountModel',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('deduction', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='优惠券额度')),
                ('total_maney', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='满减额度')),
                ('datatime', models.CharField(max_length=20, verbose_name='发放时间')),
                ('periode_of_validity', models.CharField(max_length=20, verbose_name='有效时间')),
            ],
            options={
                'verbose_name': '优惠券表',
                'verbose_name_plural': '优惠券表',
                'db_table': 't_discount',
            },
        ),
    ]