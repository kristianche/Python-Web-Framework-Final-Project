from django.test import TestCase
from django.core.exceptions import ValidationError
from BooksFace.BooksFaceApp.models import ReviewBook, Profile, Book


class ReviewBookModelTest(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(username='test_user')
        self.book = Book.objects.create(title='Test Book')

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
        with self.assertRaises(ValidationError) as context:
            ReviewBook.objects.create(**review_data)

        self.assertTrue(
            f'Ensure this value has at most {ReviewBook.REVIEW_MAX_LENGTH} characters' in str(context.exception)
        )

    def test_grade_max_value_raises_error(self):
        review_data = self.review_data.copy()
        review_data['grade'] = 11
        with self.assertRaises(ValidationError) as context:
            ReviewBook.objects.create(**review_data)

        self.assertEquals(
            f"Ensure this value is less than or equal to {ReviewBook.GRADE_MAX_VALUE}s.",  str(context.exception)
        )

    def test_grade_min_value_raises_error(self):
        review_data = self.review_data.copy()
        review_data['grade'] = -1
        with self.assertRaises(ValidationError) as context:
            ReviewBook.objects.create(**review_data)

        self.assertEquals(
            f"Ensure this value is a multiple of step size {ReviewBook.GRADE_MIN_VALUE}s.", str(context.exception)
        )

    def test_likes_increase_method_successfully(self):
        review_data = self.review_data.copy()
        review = ReviewBook.objects.create(**review_data)
        review.likes_increase()
        self.assertEquals(review.likes, 11)

    def test_str_successfully(self):
        review_data = self.review_data.copy()
        review = ReviewBook.objects.create(**review_data)
        self.assertEquals(str(review), 'test_user-Test Book-grade')

    def test_created_successfully(self):
        review_data = self.review_data.copy()
        review = ReviewBook.objects.create(**review_data)
        self.assertEquals(str(review.review), 'This is a test review for the book.')
        self.assertEquals(review.grade, 8.5)
        self.assertEquals(review.author, self.profile)
        self.assertEquals(review.book, self.book)
        self.assertEquals(review.likes, 10)