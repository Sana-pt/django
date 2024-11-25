# Generated by Django 5.1.1 on 2024-10-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookmodel',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
    ]
