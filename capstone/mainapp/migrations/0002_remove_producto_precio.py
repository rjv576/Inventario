# Generated by Django 5.0.4 on 2024-04-26 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
    ]
