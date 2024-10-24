# Generated by Django 5.1.1 on 2024-10-16 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django2', '0008_rename_userp_productuser1model_usern'),
    ]

    operations = [
        migrations.CreateModel(
            name='publishermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pb_name', models.CharField(max_length=500)),
                ('pb_address', models.CharField(max_length=500)),
                ('pb_email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='bookpbmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bpb_title', models.CharField(max_length=500)),
                ('bpb_publication_date', models.DateField()),
                ('bpb_isbn', models.CharField(max_length=13, unique=True)),
                ('bpb_publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django2.publishermodel')),
            ],
        ),
    ]
