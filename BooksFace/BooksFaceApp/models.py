from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth import models as auth_model
from .validators import check_password_number, check_password_capital_letter, check_password_lowercase_letter, check_password_special_symbol, CheckStartsWithCapitalLetter


class Profile(auth_model.AbstractUser):

    NAMES_MAX_LENGTH = 150
    NAMES_MIN_LENGTH = 2
    PASSWORD_MIN_LENGTH = 8
    LOCATION_MAX_LENGTH = 120
    LOCATION_MIN_LENGTH = 2
    FIRST_NAME_CHECK_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE = 'The first name must start with a capital letter!'
    LAST_NAME_CHECK_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE = 'The last name must start with a capital letter!'
    LOCAL_LOCATION_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE = 'The name ofthe  city/town/village must start with a capital letter!'
    COUNTRY_LOCATION_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE = "The country's name must start with a capital letter!"
    SEX_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    groups = models.ManyToManyField(auth_model.Group, related_name='user_profiles')

    user_permissions = models.ManyToManyField(auth_model.Permission, related_name='user_profiles')

    first_name = models.CharField(
        verbose_name='First Name',
        blank=False,
        null=False,
        validators=[
            MaxLengthValidator(NAMES_MAX_LENGTH),
            MinLengthValidator(NAMES_MIN_LENGTH),
            CheckStartsWithCapitalLetter(text=FIRST_NAME_CHECK_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE)
        ]
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        blank=False,
        null=False,
        validators=[
            MaxLengthValidator(NAMES_MAX_LENGTH),
            MinLengthValidator(NAMES_MIN_LENGTH),
            CheckStartsWithCapitalLetter(text=LAST_NAME_CHECK_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE)
        ]
    )
    password = models.CharField(
        null=False,
        blank=False,
        verbose_name='Password',
        validators=[
            MinLengthValidator(PASSWORD_MIN_LENGTH),
            check_password_capital_letter,
            check_password_lowercase_letter,
            check_password_special_symbol,
            check_password_number
        ]
    )
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='profile_images'
    )
    password2 = models.CharField(
        null=False,
        blank=False,
        verbose_name='Password Confirmation',
        default='password'
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Birthday',
        default=None
    )

    sex = models.CharField(
        null=True,
        blank=True,
        choices=SEX_CHOICES,
        default=None
    )

    city = models.CharField(
        null=True,
        blank=True,
        verbose_name='City/Town/Village',
        validators=[
            MinLengthValidator(LOCATION_MIN_LENGTH),
            MaxLengthValidator(LOCATION_MAX_LENGTH),
            CheckStartsWithCapitalLetter(text=LOCAL_LOCATION_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE)]
    )

    country = models.CharField(
        null=True,
        blank=True,
        verbose_name='Country',
        default=None,
        validators=[
            MinLengthValidator(LOCATION_MIN_LENGTH),
            MaxLengthValidator(LOCATION_MAX_LENGTH),
            CheckStartsWithCapitalLetter(text=COUNTRY_LOCATION_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE)]
    )

    def __str__(self):
        return self.username

    def clean(self):
        if self.password != self.password2:
            raise ValidationError("Passwords do not match.")


class Author(models.Model):

    AUTHOR_NAME_MAX_LENGTH = 120
    AUTHOR_NAME_MIN_LENGTH = 2
    BIOGRAPHY_MAX_LENGTH = 3000
    FIRST_NAME_STARTS_WITH_CAPITAL_LETTER = 'The first name of the author must start with a capital letter!'
    LAST_NAME_STARTS_WITH_CAPITAL_LETTER = 'The last name of the author must start with a capital letter!'

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='authors_images'
    )
    first_name = models.CharField(
        null=False,
        blank=False,
        verbose_name='First Name',
        validators=[
            MaxLengthValidator(AUTHOR_NAME_MAX_LENGTH),
            MinLengthValidator(AUTHOR_NAME_MIN_LENGTH),
            CheckStartsWithCapitalLetter(text=FIRST_NAME_STARTS_WITH_CAPITAL_LETTER)
        ]
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        verbose_name='Last Name',
        validators=[
            MaxLengthValidator(AUTHOR_NAME_MAX_LENGTH),
            MinLengthValidator(AUTHOR_NAME_MIN_LENGTH),
            CheckStartsWithCapitalLetter(text=LAST_NAME_STARTS_WITH_CAPITAL_LETTER)
        ]
    )

    biography = models.TextField(
        null=True,
        blank=True,
        verbose_name='Biography',
        validators=[MaxLengthValidator(BIOGRAPHY_MAX_LENGTH)]
    )

    created_by = models.CharField(
        null=False,
        blank=False,
        verbose_name='Created by',
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):

    PUBLISHER_NAME_MAX_LENGTH = 100
    PUBLISHER_NAME_MIN_LENGTH = 2
    DESCRIPTION_MAX_LENGTH = 1000
    PUBLISHER_NAME_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE = 'The name of the publisher must start with a capital letter!'

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='publisher_images'
    )
    name = models.CharField(
        null=False,
        blank=False,
        verbose_name='Name',
        validators=[
            MaxLengthValidator(PUBLISHER_NAME_MAX_LENGTH),
            MinLengthValidator(PUBLISHER_NAME_MIN_LENGTH),
            CheckStartsWithCapitalLetter(text=PUBLISHER_NAME_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE)
        ]
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
        validators=[MaxLengthValidator(DESCRIPTION_MAX_LENGTH)]
    )

    website = models.URLField(
        null=True,
        blank=True,
        unique=True,
        verbose_name='Publisher Website'
    )

    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
        verbose_name='Email'
    )

    created_by = models.CharField(
        null=False,
        blank=False,
        verbose_name='Created by',
    )

    def __str__(self):
        return self.name


class Book(models.Model):

    BOOK_TITLE_MAX_LENGTH = 120
    BOOK_TITLE_MIN_LENGTH = 2
    BOOK_TITLE_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE = 'The book title must start with a capital letter!'

    GENRE_CHOICES = (
        ('Action and Adventure Fiction', 'Action and Adventure Fiction'),
        ('Classic Fiction', 'Classic Fiction'),
        ('Contemporary Fiction', 'Contemporary Fiction'),
        ('Dystopian Fiction', 'Dystopian Fiction'),
        ('Fantasy Fiction', 'Fantasy Fiction'),
        ('Graphic Novel', 'Graphic Novel'),
        ('Historical Fiction', 'Historical Fiction'),
        ('Horror Fiction', 'Horror Fiction'),
        ('LGBTQ+ Fiction', 'LGBTQ+ Fiction'),
        ('Literary Fiction', 'Literary Fiction'),
        ('Mystery Fiction', 'Mystery Fiction'),
        ('Romance Fiction', 'Romance Fiction'),
        ('Satire Fiction', 'Satire Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Short Story', 'Short Story'),
        ('Thriller Fiction', 'Thriller Fiction'),
        ('Utopian Fiction', 'Utopian Fiction'),
        ('Western Fiction', 'Western Fiction'),
        ('Women’s Fiction', 'Women’s Fiction'),
        ('Young Adult', 'Young Adult'),
        ('Nonfiction genres', 'Nonfiction genres'),
        ('Art and Photography', 'Art and Photography'),
        ('Biography', 'Biography'),
        ('Cookbooks', 'Cookbooks'),
        ('Historical Nonfiction', 'Historical Nonfiction'),
        ('How-to and DIY', 'How-to and DIY'),
        ('Humor', 'Humor'),
        ('Memoir and Autobiography', 'Memoir and Autobiography'),
        ('Parenting', 'Parenting'),
        ('Philosophy', 'Philosophy'),
        ('Religion and Spirituality', 'Religion and Spirituality'),
        ('Self-Help', 'Self-Help'),
        ('Travel', 'Travel'),
        ('True Crime', 'True Crime'),
    )

    title = models.CharField(
        null=False,
        blank=False,
        verbose_name='Title',
        validators=[
            MaxLengthValidator(BOOK_TITLE_MAX_LENGTH),
            MinLengthValidator(BOOK_TITLE_MIN_LENGTH),
            CheckStartsWithCapitalLetter(text=BOOK_TITLE_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE)
        ]
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Author'
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='book_images',
        verbose_name='Image URL'
    )

    genre = models.CharField(
        null=False,
        blank=False,
        choices=GENRE_CHOICES,
        verbose_name='Genre'
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
        verbose_name='Publisher'
    )

    publication_date_book = models.DateField(
        null=True,
        blank=True,
        verbose_name='Book Publication Date'
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description'
    )

    reviews_counter = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name='Reviews'
    )

    created_by = models.CharField(
        null=False,
        blank=False,
        verbose_name='Created by',
    )

    def reviews_counter_increase(self):
        self.reviews_counter += 1

    def __str__(self):
        return self.title


class ReviewBook(models.Model):

    GRADE_MIN_VALUE = 0
    GRADE_MAX_VALUE = 10
    REVIEW_MAX_LENGTH = 1000

    review = models.TextField(
        null=False,
        blank=False,
        verbose_name='Review',
        validators=[MaxLengthValidator(REVIEW_MAX_LENGTH)]

    )

    grade = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(GRADE_MIN_VALUE), MaxValueValidator(GRADE_MAX_VALUE)],
        verbose_name='Book Grade',
        default=0
    )

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Review Author'
    )

    review_date = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name='Review Publishing Time',
        auto_now_add=True

    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Book'
    )

    likes = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Review Likes',
        default=0
    )

    def likes_increase(self):
        self.likes += 1

    def __str__(self):
        return f'{self.author.username}-{self.book.title}-{self.grade}'

