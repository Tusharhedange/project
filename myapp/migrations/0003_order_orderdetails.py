# Generated by Django 4.1.2 on 2022-10-31 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_alter_product_pic'),
        ('myapp', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
    ]
