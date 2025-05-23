# Generated by Django 5.1.4 on 2025-01-07 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0127_alter_college_founded_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='profile_picture',
            field=models.ImageField(default='Unknown', upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='company',
            name='profile_picture',
            field=models.ImageField(default='Unknown', upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='jobseeker_resume',
            name='profile_picture',
            field=models.ImageField(default='Unknown', upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='resume',
            name='profile_picture',
            field=models.ImageField(default='Unknown', upload_to='profile_pics/'),
        ),
    ]
