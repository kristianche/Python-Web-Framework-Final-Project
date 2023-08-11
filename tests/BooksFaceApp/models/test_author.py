from django.test import TestCase
from django.core.exceptions import ValidationError
from BooksFace.BooksFaceApp.models import Author


class AuthorModelTest(TestCase):

    def setUp(self):
        self.author_data = {
            'first_name': 'Steven',
            'last_name': 'King',
            'biography': 'Some bio...',
            'created_by': 'Admin',
        }

    def test_first_name_max_length_raises_error(self):
        author_data = self.author_data.copy()
        author_data['first_name'] = 'A' * (Author.AUTHOR_NAME_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            author = Author.objects.create(**author_data)
            author.full_clean()

    def test_first_name_min_length_raises_error(self):
        author_data = self.author_data.copy()
        author_data['first_name'] = 'A' * (Author.AUTHOR_NAME_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError):
            author = Author.objects.create(**author_data)
            author.full_clean()

    def test_first_name_starts_with_capital_letter_raises_error(self):
        author_data = self.author_data.copy()
        author_data['first_name'] = 'steven'
        with self.assertRaises(ValidationError) as context:
            author = Author.objects.create(**author_data)
            author.full_clean()

        self.assertEquals(
            f"{Author.FIRST_NAME_STARTS_WITH_CAPITAL_LETTER}", str(context.exception.messages[1])
        )

    def test_last_name_max_length_raises_error(self):
        author_data = self.author_data.copy()
        author_data['last_name'] = 'A' * (Author.AUTHOR_NAME_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            author = Author.objects.create(**author_data)
            author.full_clean()

    def test_last_name_min_length_raise_error(self):
        author_data = self.author_data.copy()
        author_data['last_name'] = 'A' * (Author.AUTHOR_NAME_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError):
            author = Author.objects.create(**author_data)
            author.full_clean()

    def test_last_name_starts_with_capital_letter_raises_error(self):
        author_data = self.author_data.copy()
        author_data['last_name'] = 'king'
        with self.assertRaises(ValidationError) as context:
            author = Author.objects.create(**author_data)
            author.full_clean()

        self.assertEquals(
            f"{Author.LAST_NAME_STARTS_WITH_CAPITAL_LETTER}", str(context.exception.messages[1])
        )

    def test_biography_max_length_raises_error(self):
        author_data = self.author_data.copy()
        author_data['biography'] = 'A' * (Author.BIOGRAPHY_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            author = Author.objects.create(**author_data)
            author.full_clean()

    def test_full_name_okay(self):
        author_data = self.author_data.copy()
        author = Author.objects.create(**author_data)
        full_name = author.full_name()
        self.assertEquals(
            full_name, 'Steven King'
        )

    def test_str_okay(self):
        author_data = self.author_data.copy()
        author = Author.objects.create(**author_data)
        self.assertEquals(
            str(author), 'Steven King'
        )

    def test_created_author_successfully(self):
        author_data = self.author_data.copy()
        author = Author.objects.create(**author_data)

        self.assertEquals(author.first_name, 'Steven')
        self.assertEquals(author.last_name, 'King')
        self.assertEquals(author.biography, 'Some bio...')
        self.assertEquals(author.created_by, 'Admin')
