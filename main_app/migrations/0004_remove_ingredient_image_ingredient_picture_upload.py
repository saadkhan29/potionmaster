# Generated by Django 4.0.2 on 2022-04-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_potions_potion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='image',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='picture_upload',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='main_app/static/images'),
        ),
    ]
