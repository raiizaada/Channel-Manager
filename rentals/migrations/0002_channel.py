# Generated by Django 4.1 on 2022-10-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_title', models.CharField(max_length=20)),
                ('channel_image', models.FileField(default=None, null=True, upload_to='channels')),
                ('channel_description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'channel',
            },
        ),
    ]
