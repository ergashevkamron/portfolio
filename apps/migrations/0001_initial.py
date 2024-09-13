# Generated by Django 5.0.6 on 2024-08-26 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='Blog')),
                ('category', models.CharField(blank=True, max_length=111, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('text', models.TextField(blank=True, max_length=150, null=True)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogSingles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('text', models.TextField(blank=True, max_length=150, null=True)),
                ('recent_post', models.CharField(blank=True, max_length=150, null=True)),
                ('archives', models.CharField(blank=True, max_length=150, null=True)),
                ('tags', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_main', models.ImageField(blank=True, null=True, upload_to='Portfolio')),
                ('image_details', models.ImageField(blank=True, null=True, upload_to='Portfolio_details')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=111, null=True)),
                ('upload_date', models.CharField(blank=True, max_length=111, null=True)),
                ('client', models.CharField(blank=True, max_length=100, null=True)),
                ('project_date', models.CharField(blank=True, max_length=202, null=True)),
                ('project_url', models.URLField()),
                ('about_project', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('short_comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=222, null=True, verbose_name='ism')),
                ('last_name', models.CharField(max_length=200, verbose_name='familya')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('job', models.CharField(max_length=200, verbose_name='kasbi')),
                ('phone_number', models.CharField(max_length=30, verbose_name='telofon raqami')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='pochta manzil')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('about_me', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='skill nomi')),
                ('level', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.user')),
            ],
        ),
    ]
