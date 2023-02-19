# Generated by Django 4.1 on 2022-12-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0066_remove_activity_user_id_remove_attributes_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='coutry',
            new_name='country',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='no_of_properties',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='property_role',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
