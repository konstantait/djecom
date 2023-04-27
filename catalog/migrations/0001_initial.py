# Generated by Django 4.2 on 2023-04-25 15:25

import core.mixins.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sort_order', models.IntegerField(default=0, verbose_name='Sort')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sort_order', models.IntegerField(default=0, verbose_name='Sort')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Enabled'), (1, 'Disabled')], default=0)),
                ('sort_order', models.IntegerField(default=0, verbose_name='Sort')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='placeholder.jpg', upload_to=core.mixins.models.upload_to)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Enabled'), (1, 'Disabled')], default=0)),
                ('sort_order', models.IntegerField(default=0, verbose_name='Sort')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=18, validators=[django.core.validators.MinValueValidator(0)])),
                ('model', models.CharField(blank=True, default='', max_length=64)),
                ('sku', models.CharField(max_length=64, unique=True)),
                ('attributes', models.ManyToManyField(blank=True, related_name='products', to='catalog.attribute')),
                ('categories', models.ManyToManyField(blank=True, related_name='products', to='catalog.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Enabled'), (1, 'Disabled')], default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('rating', models.PositiveSmallIntegerField(choices=[(0, 'Poor'), (1, 'Fair'), (2, 'Good'), (3, 'Very good'), (4, 'Excellent')], default=4)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='catalog.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='catalog.attributegroup', verbose_name='Group'),
        ),
    ]
