# Generated by Django 4.2.2 on 2023-06-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepic.png', upload_to='profile_pictures'),
        ),
    ]