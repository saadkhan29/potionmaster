# Generated by Django 4.0.2 on 2022-04-05 22:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_potion_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.CreateModel(
            name='IngredientQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(1))),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ingredient')),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='quantity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ingredientquantity'),
        ),
    ]
