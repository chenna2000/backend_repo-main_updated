# Generated by Django 5.1.4 on 2025-01-07 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0132_jobseeker_resume_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker_resume',
            name='Attachment',
        ),
    ]
