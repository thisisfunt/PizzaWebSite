# Generated by Django 3.1.7 on 2021-03-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listProducts', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('house', models.CharField(max_length=50)),
                ('intercom', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='product_in_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idOrder', models.IntegerField()),
                ('idProduct', models.IntegerField()),
            ],
        ),
    ]
