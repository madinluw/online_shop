# Generated by Django 4.1.7 on 2023-04-11 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code',
            field=models.UUIDField(blank=True, null=True, unique=True),
        ),
    ]
