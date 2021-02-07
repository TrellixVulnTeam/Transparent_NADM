# Generated by Django 3.1.5 on 2021-01-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=10000.0, max_digits=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='rewards',
            field=models.DecimalField(decimal_places=2, default=10000.0, max_digits=200),
        ),
    ]