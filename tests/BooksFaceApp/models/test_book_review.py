from django.test import TestCase
from django.core.exceptions import ValidationError
from BooksFace.BooksFaceApp.models import ReviewBook, Profile, Book, Author, Publisher


class ReviewBookModelTest(TestCase):
    def setUp(self):
        self.profile_data = {
            'username': 'test_user',
            'password': 'Password123!',
            'password2': 'Password123!',
            'first_name': 'John',
            'last_name': 'Doe',
            'birthday': '1990-01-01',
            'city': 'Test City',
            'country': 'Test Country',
            'sex': 'Male'
        }
        self.profile = Profile.objects.create(**self.profile_data)

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
        self.book = Book.objects.create(**self.book_data)

        self.review_data = {
            'review': 'This is a test review for the book.',
            'grade': 8.5,
            'author': self.profile,
            'book': self.book,
            'likes': 10,
        }

    def test_review_max_length_raises_error(self):
        review_data = self.review_data.copy()
        review_data['review'] = 'A' * (ReviewBook.REVIEW_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            review = ReviewBook.objects.create(**review_data)
            review.full_clean()

    def test_grade_max_value_raises_error(self):
        review_data = self.review_data.copy()
        review_data['grade'] = 11
        with self.assertRaises(ValidationError):
            review = ReviewBook.objects.create(**review_data)
            review.full_clean()

    def test_grade_min_value_raises_error(self):
        review_data = self.review_data.copy()
        review_data['grade'] = -1
        with self.assertRaises(ValidationError):
            review = ReviewBook.objects.create(**review_data)
            review.full_clean()

    def test_likes_increase_method_successfully(self):
        review_data = self.review_data.copy()
        review = ReviewBook.objects.create(**review_data)
        review.likes_increase()
        self.assertEquals(review.likes, 11)

    def test_str_successfully(self):
        review_data = self.review_data.copy()
        review = ReviewBook.objects.create(**review_data)
        self.assertEquals(str(review), 'test_user-Test Book-8.5')

    def test_created_successfully(self):
        review_data = self.review_data.copy()
        review = ReviewBook.objects.create(**review_data)
        self.assertEquals(str(review.review), 'This is a test review for the book.')
        self.assertEquals(review.grade, 8.5)
        self.assertEquals(review.author, self.profile)
        self.assertEquals(review.book, self.book)
        self.assertEquals(review.likes, 10)