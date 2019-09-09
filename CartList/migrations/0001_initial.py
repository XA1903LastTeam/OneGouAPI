# Generated by Django 2.0.1 on 2019-09-09 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order_listModel',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=50, verbose_name='下单时间')),
                ('order_statud', models.IntegerField(choices=[(0, '待支付'), (1, '已支付'), (2, '已取消'), (3, '待发货'), (4, '已发货'), (5, '已完成')], verbose_name='订单状态')),
                ('count', models.IntegerField(verbose_name='商品数量')),
                ('card_id', models.IntegerField(verbose_name='所属购物车')),
                ('goods_id', models.ManyToManyField(db_table='t_goods_order_list', related_name='goods', to='Goods.GoodsModel', verbose_name='商品ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order_listmodel',
            name='order_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='CartList.OrderModel', verbose_name='订单ID'),
        ),
    ]
