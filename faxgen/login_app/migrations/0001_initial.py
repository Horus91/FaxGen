# Generated by Django 5.0.1 on 2024-01-18 16:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft', models.CharField(blank=True, choices=[('CDMT', 'CDMT'), ('B74X', 'B74X'), ('B737', 'B737'), ('RJ10', 'RJ10'), ('G650', 'G650'), ('G550', 'G550'), ('XLS+', 'XLS+'), ('BE35', 'BE35'), ('AW13', 'AW13')], max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
