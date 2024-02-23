# Generated by Django 5.0.2 on 2024-02-22 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flightmandu', '0006_delete_customerinfo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userinfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
