# Generated by Django 4.2.7 on 2024-04-18 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_us',
            old_name='problem',
            new_name='message',
        ),
    ]
