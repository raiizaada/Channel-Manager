# Generated by Django 4.1 on 2023-01-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0086_country_country_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_instruction', models.CharField(max_length=100)),
                ('checkout_instruction', models.CharField(max_length=100)),
                ('checkin_contact', models.CharField(max_length=100)),
                ('key_collection', models.CharField(max_length=100)),
                ('telephone_country', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=3000)),
                ('instructions', models.TextField(max_length=3000)),
                ('attach_instruction', models.FileField(upload_to='rentals-instruction')),
                ('checkin_from', models.CharField(max_length=100)),
                ('checkout_until', models.CharField(max_length=100)),
                ('airport_instruction', models.CharField(max_length=100)),
                ('property_directions', models.TextField(max_length=3000)),
                ('status', models.BooleanField(default=True)),
                ('user_id', models.IntegerField()),
                ('rental_id', models.IntegerField()),
            ],
            options={
                'db_table': 'rental_instruction',
            },
        ),
    ]
