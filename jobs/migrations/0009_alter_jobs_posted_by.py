# Generated by Django 4.2.7 on 2024-03-11 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_user'),
        ('jobs', '0008_remove_jobapplication_skills_jobapplication_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]
