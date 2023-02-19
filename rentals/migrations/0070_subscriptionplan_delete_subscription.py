# Generated by Django 4.1 on 2022-12-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0069_subscription_tenure'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('tenure', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.IntegerField()),
                ('start_date', models.CharField(max_length=200, unique=True)),
                ('expiry_date', models.CharField(max_length=200, unique=True)),
                ('subscription_id', models.IntegerField()),
            ],
            options={
                'db_table': 'subscription_plan',
            },
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]