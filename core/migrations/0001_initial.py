# Generated by Django 4.0.2 on 2022-04-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('message', models.TextField(help_text='Buraya mesajinizi daxil edin!', verbose_name='Message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsLatest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('description', models.TextField(verbose_name='DESCRIPTION')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=40, verbose_name='EMAIL')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
