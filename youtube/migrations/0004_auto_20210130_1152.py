# Generated by Django 3.1.5 on 2021-01-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_auto_20210129_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
