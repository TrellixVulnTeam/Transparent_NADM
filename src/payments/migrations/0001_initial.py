# Generated by Django 3.1.5 on 2021-01-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, default='', max_length=100)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('rewards', models.DecimalField(decimal_places=2, max_digits=200)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=200)),
            ],
        ),
    ]