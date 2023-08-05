# Generated by Django 4.2.3 on 2023-08-04 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksFaceApp', '0029_alter_profile_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='likes',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Action and Adventure Fiction', 'Action and Adventure Fiction'), ('Classic Fiction', 'Classic Fiction'), ('Contemporary Fiction', 'Contemporary Fiction'), ('Dystopian Fiction', 'Dystopian Fiction'), ('Fantasy Fiction', 'Fantasy Fiction'), ('Graphic Novel', 'Graphic Novel'), ('Historical Fiction', 'Historical Fiction'), ('Horror Fiction', 'Horror Fiction'), ('LGBTQ+ Fiction', 'LGBTQ+ Fiction'), ('Literary Fiction', 'Literary Fiction'), ('Mystery Fiction', 'Mystery Fiction'), ('Romance Fiction', 'Romance Fiction'), ('Satire Fiction', 'Satire Fiction'), ('Science Fiction', 'Science Fiction'), ('Short Story', 'Short Story'), ('Thriller Fiction', 'Thriller Fiction'), ('Utopian Fiction', 'Utopian Fiction'), ('Western Fiction', 'Western Fiction'), ('Women’s Fiction', 'Women’s Fiction'), ('Young Adult', 'Young Adult'), ('Nonfiction genres', 'Nonfiction genres'), ('Art and Photography', 'Art and Photography'), ('Biography', 'Biography'), ('Cookbooks', 'Cookbooks'), ('Historical Nonfiction', 'Historical Nonfiction'), ('How-to and DIY', 'How-to and DIY'), ('Humor', 'Humor'), ('Memoir and Autobiography', 'Memoir and Autobiography'), ('Parenting', 'Parenting'), ('Philosophy', 'Philosophy'), ('Religion and Spirituality', 'Religion and Spirituality'), ('Self-Help', 'Self-Help'), ('Travel', 'Travel'), ('True Crime', 'True Crime'), ('Drama', 'Drama'), ('Comedy', 'Comedy')], verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
        ),
    ]
