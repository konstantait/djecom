# Generated by Django 4.2.1 on 2023-05-24 14:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_alter_product_options_remove_product_attributes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bookmarked_by',
            field=models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]