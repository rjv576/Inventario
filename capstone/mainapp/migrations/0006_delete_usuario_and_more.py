# Generated by Django 5.0.4 on 2024-04-28 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_usuario_email_usuario_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='createed_at',
            new_name='created_at',
        ),
    ]