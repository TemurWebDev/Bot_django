# Generated by Django 3.2.4 on 2022-05-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0004_tguser_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='phon_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]