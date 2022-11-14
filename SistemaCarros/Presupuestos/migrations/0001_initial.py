# Generated by Django 3.2.10 on 2022-06-09 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tecnicos', '0001_initial'),
        ('carros', '0001_initial'),
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presupuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garantia', models.CharField(default=0, max_length=255)),
                ('total_parte', models.FloatField(blank=True, null=True)),
                ('descuentoTotal_parte', models.FloatField(default=0, null=True)),
                ('total_manaobra', models.FloatField(blank=True, null=True)),
                ('descuentoTotal_manaobra', models.FloatField(default=0, null=True)),
                ('total_paid', models.FloatField(default=0, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('CANCELED', 'canceled')], default='PENDING', max_length=10)),
                ('resumen', models.CharField(blank=True, max_length=255)),
                ('register_time', models.DateTimeField(auto_now=True)),
                ('carro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carros.carro')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Clientes.clientes')),
                ('tecnicos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tecnicos.tecnicos')),
            ],
        ),
    ]
