# Generated by Django 4.2.7 on 2024-04-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Company_Logo',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
