# Generated by Django 5.1.1 on 2024-10-23 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django2', '0009_publishermodel_bookpbmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=500)),
                ('course_code', models.CharField(max_length=200, unique=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='studentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django2.coursemodel')),
            ],
        ),
    ]
