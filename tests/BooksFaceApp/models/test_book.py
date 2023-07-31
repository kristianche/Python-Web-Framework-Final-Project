from django.test import TestCase
from django.core.exceptions import ValidationError
from BooksFace.BooksFaceApp.models import Book, Author, Publisher


class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name='John', last_name='Doe')
        self.publisher = Publisher.objects.create(name='Test Publisher')

        self.book_data = {
            'title': 'Test Book',
            'author': self.author,
            'genre': 'Science Fiction',
            'publisher': self.publisher,
            'publication_date_book': '2023-01-01',
            'description': 'This is a test book.',
            'reviews_counter': 6,
            'created_by': 'Admin'
        }

    def test_title_max_length_raises_error(self):
        book_data = self.book_data.copy()
        book_data['title'] = 'A' * (Book.BOOK_TITLE_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            book = Book.objects.create(**book_data)
            book.full_clean()

    def test_title_min_length_raises_error(self):
        book_data = self.book_data.copy()
        book_data['title'] = 'A' * (Book.BOOK_TITLE_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError):
            book = Book.objects.create(**book_data)
            book.full_clean()

    def test_title_starts_with_capital_letter_raises_error(self):
        book_data = self.book_data.copy()
        book_data['title'] = 'test book'
        with self.assertRaises(ValidationError) as context:
            book = Book.objects.create(**book_data)
            book.full_clean()

        self.assertEquals(Book.BOOK_TITLE_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE, str(context.exception.messages[0]))

    def test_reviews_counter_increase_successfully(self):
        book_data = self.book_data.copy()
        book = Book.objects.create(**book_data)
        book.reviews_counter_increase()

        self.assertEquals(book.reviews_counter, 7)

    def test_str_successfully(self):
        book_data = self.book_data.copy()
        book = Book.objects.create(**book_data)

        self.assertEquals(str(book), 'Test Book')

    def test_created_successfully(self):
        book_data = self.book_data.copy()
        book = Book.objects.create(**book_data)

        self.assertEquals(book.title, 'Test Book')
        self.assertEquals(book.author, self.author)
        self.assertEquals(book.genre, 'Science Fiction')
        self.assertEquals(book.publisher, self.publisher)
        self.assertEquals(str(book.publication_date_book), '2023-01-01')
        self.assertEquals(book.reviews_counter, 6)
        self.assertEquals(book.created_by, 'Admin')
