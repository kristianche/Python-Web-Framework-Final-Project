# Generated by Django 4.2.3 on 2023-08-14 09:25

import BooksFace.BooksFaceApp.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksFaceApp', '0037_alter_profile_first_name_alter_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, null=True, validators=[BooksFace.BooksFaceApp.validators.CheckStartsWithCapitalLetter(text='The first name must start with a capital letter!'), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(150)], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, null=True, validators=[BooksFace.BooksFaceApp.validators.CheckStartsWithCapitalLetter(text='The last name must start with a capital letter!'), django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(150)], verbose_name='Last Name'),
        ),
    ]
