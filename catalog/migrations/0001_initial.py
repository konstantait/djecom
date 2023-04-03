# Generated by Django 4.1.7 on 2023-04-03 10:09

import core.mixins.models
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=core.mixins.models.upload_to)),
                ('status', models.BooleanField(default=True)),
                ('sort_order', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField()),
                ('code', models.CharField(max_length=64)),
                ('status', models.BooleanField(default=True)),
                ('discount_type', models.PositiveSmallIntegerField(choices=[(0, 'cash'), (1, 'percent')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=core.mixins.models.upload_to)),
                ('status', models.BooleanField(default=True)),
                ('sort_order', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('model', models.CharField(max_length=64)),
                ('sku', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=18, validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
