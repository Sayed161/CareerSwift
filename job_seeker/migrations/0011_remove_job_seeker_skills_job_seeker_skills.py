# Generated by Django 4.2.7 on 2024-02-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0010_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_seeker',
            name='skills',
        ),
        migrations.AddField(
            model_name='job_seeker',
            name='skills',
            field=models.ManyToManyField(to='job_seeker.skill'),
        ),
    ]
