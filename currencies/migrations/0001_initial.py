# Generated by Django 4.2.1 on 2023-05-17 16:50

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Enabled'), (1, 'Disabled')], default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('title', models.CharField(blank=True, default='', max_length=32)),
                ('code', models.CharField(max_length=3, unique=True)),
                ('symbol_left', models.CharField(blank=True, default='', max_length=12)),
                ('symbol_right', models.CharField(blank=True, default='', max_length=12)),
                ('decimal_place', models.PositiveIntegerField(default=2)),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=18, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]