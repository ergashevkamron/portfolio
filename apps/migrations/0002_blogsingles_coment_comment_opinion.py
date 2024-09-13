# Generated by Django 5.0.6 on 2024-09-06 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsingles',
            name='coment',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.user')),
            ],
        ),
    ]