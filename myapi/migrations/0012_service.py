# Generated by Django 3.2.5 on 2021-09-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0011_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('partner', models.CharField(max_length=60)),
                ('branches', models.CharField(blank=True, max_length=60, null=True)),
                ('product_type', models.CharField(max_length=60)),
                ('approx_fee', models.CharField(max_length=60)),
                ('revenue_type', models.CharField(blank=True, max_length=60, null=True)),
                ('duration', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
