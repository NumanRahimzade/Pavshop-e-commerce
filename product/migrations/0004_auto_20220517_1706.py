# Generated by Django 3.1 on 2022-05-17 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220513_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyname',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, related_name='propertynames', to='product.category'),
        ),
    ]