# Generated by Django 4.2.3 on 2023-08-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksFaceApp', '0022_remove_profile_email_remove_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, default=None, null=True, verbose_name='Description'),
        ),
    ]
