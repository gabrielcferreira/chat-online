# Generated by Django 5.1.3 on 2024-11-29 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='title',
            new_name='text',
        ),
    ]
