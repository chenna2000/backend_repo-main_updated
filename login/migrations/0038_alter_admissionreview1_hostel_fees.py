# Generated by Django 5.1.5 on 2025-03-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0037_alter_admissionreview1_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionreview1',
            name='hostel_fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
