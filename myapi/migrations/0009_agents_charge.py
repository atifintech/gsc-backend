# Generated by Django 3.2.5 on 2021-09-11 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_students_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='agents',
            name='charge',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]