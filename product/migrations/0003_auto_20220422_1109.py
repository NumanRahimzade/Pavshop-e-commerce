# Generated by Django 3.1 on 2022-04-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tag'),
        ('product', '0002_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AddField(
            model_name='productversion',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='product_tags', to='core.Tag'),
        ),
    ]
