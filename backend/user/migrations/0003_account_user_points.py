# Generated by Django 4.1.7 on 2023-02-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user_points',
            field=models.CharField(default=0, max_length=120),
        ),
    ]
