# Generated by Django 5.0.3 on 2024-03-28 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_options_product_price_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompanyManufacturingChoices',
            new_name='CompanyManufacturing',
        ),
        migrations.RenameModel(
            old_name='ShelfLifeChoices',
            new_name='ShelfLife',
        ),
    ]