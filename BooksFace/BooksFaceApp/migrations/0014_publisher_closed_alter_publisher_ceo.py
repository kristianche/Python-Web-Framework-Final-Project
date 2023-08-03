# Generated by Django 4.2.3 on 2023-08-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksFaceApp', '0013_publisher_ceo_publisher_country_publisher_founded'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='closed',
            field=models.CharField(blank=True, null=True, unique=True, verbose_name='Closed on'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='ceo',
            field=models.CharField(blank=True, null=True, unique=True, verbose_name='Ceo'),
        ),
    ]