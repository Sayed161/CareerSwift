# Generated by Django 4.2.7 on 2024-01-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_jobs_benifits_jobs_post_jobs_responsibities_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.TextField(default=None),
        ),
    ]
