# Generated by Django 4.2.3 on 2023-08-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksFaceApp', '0034_alter_author_created_by_alter_book_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=None, verbose_name='Username'),
            preserve_default=False,
        ),
    ]
