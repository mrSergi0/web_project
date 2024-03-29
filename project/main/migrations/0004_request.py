# Generated by Django 5.0.1 on 2024-01-28 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_image_alter_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('message', models.TextField(max_length=250)),
            ],
        ),
    ]
