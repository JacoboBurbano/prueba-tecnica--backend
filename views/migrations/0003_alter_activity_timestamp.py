# Generated by Django 5.1.6 on 2025-02-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0002_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
