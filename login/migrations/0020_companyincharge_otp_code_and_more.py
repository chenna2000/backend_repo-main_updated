# Generated by Django 5.1.4 on 2024-12-31 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_remove_companyincharge_user_remove_consultant_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyincharge',
            name='otp_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='companyincharge',
            name='otp_generated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
