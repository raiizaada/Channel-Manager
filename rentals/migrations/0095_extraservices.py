# Generated by Django 4.1 on 2023-01-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0094_rentaltax'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_provided', models.CharField(max_length=100)),
                ('fee_basis', models.CharField(max_length=100)),
                ('service_price', models.CharField(max_length=100)),
                ('earliest_guest_order', models.CharField(max_length=100)),
                ('latest_guest_order', models.CharField(max_length=100)),
                ('guest_cancel_order', models.CharField(max_length=100)),
                ('extra_message', models.TextField(max_length=3000)),
                ('status', models.BooleanField(default=True)),
                ('user_id', models.IntegerField()),
                ('rental_id', models.IntegerField()),
            ],
            options={
                'db_table': 'rental_extra_services',
            },
        ),
    ]