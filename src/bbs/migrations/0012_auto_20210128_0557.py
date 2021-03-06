# Generated by Django 3.1.5 on 2021-01-28 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bbs', '0011_remove_book_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='end',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='start',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='staff',
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schedule',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
