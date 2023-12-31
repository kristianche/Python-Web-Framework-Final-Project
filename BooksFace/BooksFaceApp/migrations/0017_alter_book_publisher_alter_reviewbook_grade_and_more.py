# Generated by Django 4.2.3 on 2023-08-04 10:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BooksFaceApp', '0016_alter_profile_options_alter_profile_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BooksFaceApp.publisher', verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='reviewbook',
            name='grade',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Book Grade'),
        ),
        migrations.AlterField(
            model_name='reviewbook',
            name='review',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(3000)], verbose_name='Review'),
        ),
    ]
