# Generated by Django 4.1.7 on 2023-02-27 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_user_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_image_link', models.CharField(max_length=500, null=True)),
                ('app_name', models.CharField(max_length=500, null=True)),
                ('app_link', models.CharField(max_length=500, null=True)),
                ('app_category', models.CharField(max_length=500, null=True)),
                ('sub_category', models.CharField(max_length=500, null=True)),
                ('points', models.CharField(max_length=500, null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name_app', to='user.apps')),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
