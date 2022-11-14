# Generated by Django 3.2.10 on 2022-06-09 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer', models.CharField(blank=True, max_length=255, null=True)),
                ('codigoInventory', models.CharField(blank=True, max_length=255)),
                ('invoiceNumber', models.IntegerField()),
                ('descriptionInventory', models.CharField(blank=True, max_length=255, null=True)),
                ('quantityInventory', models.IntegerField(default=0)),
                ('unitPriceInventory', models.IntegerField()),
                ('minimumInventory', models.IntegerField()),
                ('status', models.CharField(choices=[('Ok', 'Ok'), ('Pending', 'Pending')], default='Ok', max_length=255)),
                ('fecha_registro', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]