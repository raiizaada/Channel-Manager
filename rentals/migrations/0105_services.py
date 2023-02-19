# Generated by Django 4.1 on 2023-01-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0104_channelmanagement_rental_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'services',
            },
        ),
    ]