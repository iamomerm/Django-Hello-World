# Generated by Django 5.0.6 on 2024-06-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='banner',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
