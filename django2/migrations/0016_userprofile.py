# Generated by Django 5.1.1 on 2024-10-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django2', '0015_formmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('date_of_birth', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('bio', models.TextField(null=True)),
            ],
        ),
    ]
