# Generated by Django 4.1 on 2022-12-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0072_subscriptionplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='expiry_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='start_date',
            field=models.CharField(max_length=100),
        ),
    ]