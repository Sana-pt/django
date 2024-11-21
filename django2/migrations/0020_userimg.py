# Generated by Django 5.1.1 on 2024-11-01 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django2', '0019_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='userimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ui_name', models.CharField(max_length=100)),
                ('ui_age', models.IntegerField()),
                ('ui_img', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
