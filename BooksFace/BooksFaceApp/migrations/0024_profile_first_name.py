# Generated by Django 4.2.3 on 2023-08-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksFaceApp', '0023_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, null=True),
        ),
    ]
