# Generated by Django 3.2.8 on 2021-10-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211018_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='complete_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Cost'),
        ),
    ]
