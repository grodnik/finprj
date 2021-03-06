# Generated by Django 3.2.8 on 2021-10-18 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Project Name')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('create_date', models.DateTimeField(verbose_name='Date Identified')),
                ('orig_est_cost', models.DecimalField(blank=True, decimal_places=0, max_digits=7, verbose_name='Estimated Cost')),
                ('start_date', models.DateTimeField(blank=True, verbose_name='Start Date')),
                ('complete_date', models.DateTimeField(blank=True, verbose_name='Date Complete')),
                ('complete_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Cost')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateTimeField(verbose_name='Invoice Date')),
                ('paid_date', models.DateTimeField(verbose_name='Paid Date')),
                ('vendor', models.CharField(max_length=120, verbose_name='Vendor')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Amount')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.project')),
            ],
        ),
    ]
