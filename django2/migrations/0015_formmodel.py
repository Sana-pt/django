# Generated by Django 5.1.1 on 2024-10-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django2', '0014_rename_bookins_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='formmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
