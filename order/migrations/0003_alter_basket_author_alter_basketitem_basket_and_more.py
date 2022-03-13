# Generated by Django 4.0.2 on 2022-03-11 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_basket_author_basketitem_basket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order.basket'),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='productVersion',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.productversion'),
        ),
        migrations.AlterField(
            model_name='order',
            name='basket',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='order.basket'),
        ),
    ]