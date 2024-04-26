# Generated by Django 4.2.7 on 2024-04-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_employee_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='About',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='Company_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='company_mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
