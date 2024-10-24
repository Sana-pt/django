# Generated by Django 5.1.1 on 2024-10-16 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django2', '0006_alter_blogmodel_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='user1model',
            fields=[
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=500)),
                ('u_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='productuser1model',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=500)),
                ('userp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django2.user1model')),
            ],
        ),
    ]