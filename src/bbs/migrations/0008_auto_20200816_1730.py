# Generated by Django 3.1 on 2020-08-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0007_auto_20200816_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
