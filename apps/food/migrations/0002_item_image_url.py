# Generated by Django 4.2.2 on 2023-06-09 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/6/62/Image_unavailable.png', max_length=500),
        ),
    ]
