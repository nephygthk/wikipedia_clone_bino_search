# Generated by Django 4.2.3 on 2023-07-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture_1',
            field=models.FileField(default='default-img.jpg', upload_to='profile_pictures'),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture_2',
            field=models.FileField(default='default-img.jpg', upload_to='profile_pictures'),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture_3',
            field=models.FileField(default='default-img.jpg', upload_to='profile_pictures'),
        ),
    ]
