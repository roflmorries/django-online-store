# Generated by Django 4.0.5 on 2022-07-29 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_product_comment_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='product',
            new_name='product_id',
        ),
    ]