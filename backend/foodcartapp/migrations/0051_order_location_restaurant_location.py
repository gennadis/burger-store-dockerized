# Generated by Django 4.0.4 on 2022-05-18 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_alter_location_latitude_alter_location_longitude'),
        ('foodcartapp', '0050_alter_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='locations.location', verbose_name='локация'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurants', to='locations.location', verbose_name='локация'),
        ),
    ]
