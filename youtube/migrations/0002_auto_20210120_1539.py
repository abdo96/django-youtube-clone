# Generated by Django 3.1.5 on 2021-01-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
