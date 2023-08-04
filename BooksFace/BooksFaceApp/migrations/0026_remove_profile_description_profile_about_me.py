# Generated by Django 4.2.3 on 2023-08-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksFaceApp', '0025_remove_profile_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.CharField(blank=True, default=None, null=True, verbose_name='About Me'),
        ),
    ]