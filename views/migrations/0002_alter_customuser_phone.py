# Generated by Django 5.1.6 on 2025-02-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
