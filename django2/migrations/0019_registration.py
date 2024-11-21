# Generated by Django 5.1.1 on 2024-11-01 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django2', '0018_alter_post_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
            ],
        ),
    ]