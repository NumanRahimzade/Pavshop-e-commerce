# Generated by Django 3.2.13 on 2022-06-13 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='basketitems', to='order.basket'),
        ),
    ]