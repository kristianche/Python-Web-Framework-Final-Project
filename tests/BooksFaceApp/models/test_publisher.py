from django.test import TestCase
from django.core.exceptions import ValidationError
from BooksFace.BooksFaceApp.models import Publisher


class PublisherModelTest(TestCase):
    def setUp(self):
        self.publisher_data = {
            'name': 'Vikings',
            'description': 'Some description...',
            'website': 'https://www.penguin.com/overview-vikingbooks/',
            'email': 'vikings@gmail.com',
            'created_by': 'Admin'
        }

    def test_name_max_length_raises_error(self):
        publisher_data = self.publisher_data.copy()
        publisher_data['name'] = 'A' * (Publisher.PUBLISHER_NAME_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            publisher = Publisher.objects.create(**publisher_data)
            publisher.full_clean()

    def test_name_min_length_raises_error(self):
        publisher_data = self.publisher_data.copy()
        publisher_data['name'] = 'A' * (Publisher.PUBLISHER_NAME_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError):
            publisher = Publisher.objects.create(**publisher_data)
            publisher.full_clean()

    def test_name_starts_with_capital_letter_raises_error(self):
        publisher_data = self.publisher_data.copy()
        publisher_data['name'] = 'vikings'
        with self.assertRaises(ValidationError)as context:
            publisher = Publisher.objects.create(**publisher_data)
            publisher.full_clean()

        self.assertEqual(str(context.exception.messages[0]), Publisher.PUBLISHER_NAME_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE)

    def test_description_max_length_raises_error(self):
        publisher_data = self.publisher_data.copy()
        publisher_data['description'] = 'A' * (Publisher.DESCRIPTION_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            publisher = Publisher.objects.create(**publisher_data)
            publisher.full_clean()

    def test_str_successfully(self):
        publisher_data = self.publisher_data.copy()
        publisher = Publisher.objects.create(**publisher_data)

        self.assertEquals(str(publisher), 'Vikings')

    def test_created_object_successfully(self):
        publisher_data = self.publisher_data.copy()
        publisher = Publisher.objects.create(**publisher_data)

        self.assertEquals(publisher.name, 'Vikings')
        self.assertEquals(publisher.description, 'Some description...')
        self.assertEquals(publisher.website, 'https://www.penguin.com/overview-vikingbooks/')
        self.assertEquals(publisher.email, 'vikings@gmail.com')
        self.assertEquals(publisher.created_by, 'Admin')