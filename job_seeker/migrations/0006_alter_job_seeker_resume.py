# Generated by Django 4.2.7 on 2024-01-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0005_remove_job_seeker_birth_date_remove_job_seeker_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_seeker',
            name='resume',
            field=models.TextField(default=None),
        ),
    ]
