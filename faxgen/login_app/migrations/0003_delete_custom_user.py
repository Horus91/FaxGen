# Generated by Django 5.0.1 on 2024-01-08 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_custom_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Custom_User',
        ),
    ]
