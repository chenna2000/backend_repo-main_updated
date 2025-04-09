# Generated by Django 5.1.4 on 2025-01-09 08:01

import django.db.models.deletion # type: ignore
from django.db import migrations, models # type: ignore


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0139_alter_collegeenquiry_new_user_and_more'),
        ('login', '0026_remove_jobseeker_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeenquiry',
            name='new_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.new_user'),
        ),
        migrations.AlterField(
            model_name='collegeenquiry',
            name='university_in_charge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.universityincharge'),
        ),
    ]
