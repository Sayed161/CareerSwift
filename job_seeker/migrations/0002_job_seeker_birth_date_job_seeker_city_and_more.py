# Generated by Django 4.2.7 on 2024-01-14 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_seeker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_seeker',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job_seeker',
            name='city',
            field=models.CharField(default=None, max_length=155),
        ),
        migrations.AddField(
            model_name='job_seeker',
            name='country',
            field=models.CharField(default=None, max_length=155),
        ),
        migrations.AddField(
            model_name='job_seeker',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], default=None, max_length=25),
        ),
        migrations.AddField(
            model_name='job_seeker',
            name='post_code',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='job_seeker',
            name='street_address',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='job_seeker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seeker', to=settings.AUTH_USER_MODEL),
        ),
    ]
