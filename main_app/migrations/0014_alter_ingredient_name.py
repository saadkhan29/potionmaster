# Generated by Django 4.0.3 on 2022-04-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_rename_ingredientquantity_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
