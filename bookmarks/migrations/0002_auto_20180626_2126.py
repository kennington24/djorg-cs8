# Generated by Django 2.0.6 on 2018-06-26 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='url',
            field=models.TextField(max_length=200),
        ),
    ]