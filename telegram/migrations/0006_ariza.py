# Generated by Django 3.2.4 on 2022-05-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0005_tguser_phon_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ariza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=255)),
            ],
        ),
    ]
