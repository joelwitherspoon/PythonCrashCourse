# Generated by Django 3.0.5 on 2020-04-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200419_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
