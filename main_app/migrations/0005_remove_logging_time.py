# Generated by Django 4.1.5 on 2023-02-07 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_logging'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logging',
            name='time',
        ),
    ]
