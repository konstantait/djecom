# Generated by Django 4.2.1 on 2023-06-02 07:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_alter_currency_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=18, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]