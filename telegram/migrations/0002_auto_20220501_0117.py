# Generated by Django 3.2.4 on 2022-04-30 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tguser',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tguser',
            name='updated_at',
        ),
    ]
