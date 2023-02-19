# Generated by Django 4.1 on 2022-11-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0039_rental_activities_id_rental_amenities_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'attributes',
            },
        ),
    ]