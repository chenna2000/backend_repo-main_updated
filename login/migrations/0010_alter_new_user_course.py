# Generated by Django 4.2.15 on 2024-10-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_companyincharge_token_consultant_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='course',
            field=models.CharField(default='B-Tech', max_length=50),
        ),
    ]
