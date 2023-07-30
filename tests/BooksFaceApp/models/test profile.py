from django.contrib.auth.models import Group, Permission
from django.test import TestCase
from django.core.exceptions import ValidationError
from BooksFace.BooksFaceApp.models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='Test Group')
        self.permission = Permission.objects.create(name='Test Permission')
        self.profile_data = {
            'username': 'test_user',
            'password': 'Password123!',
            'password2': 'Password123!',
            'first_name': 'John',
            'last_name': 'Doe',
            'birthday': '1990-01-01',
            'city': 'Test City',
            'country': 'Test Country',
            'sex': 'Male',
        }

    def test_first_name_max_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['first_name'] = 'A' * (Profile.NAMES_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(
            f'Ensure this value has at most {Profile.NAMES_MAX_LENGTH} characters' in str(context.exception)
        )

    def test_first_name_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['first_name'] = 'A' * (Profile.NAMES_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(
            f'Ensure this value has at most {Profile.NAMES_MIN_LENGTH} characters' in str(context.exception)
        )

    def test_first_name_starts_with_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['first_name'] = 'john'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertEquals(
            f"{Profile.FIRST_NAME_CHECK_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE}", str(context.exception)
        )

    def test_last_name_max_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['last_name'] = 'A' * (Profile.NAMES_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(
            f'Ensure this value has at most {Profile.NAMES_MAX_LENGTH} characters' in str(context.exception)
        )

    def test_last_name_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['last_name'] = 'A' * (Profile.NAMES_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(
            f'Ensure this value has at most {Profile.NAMES_MIN_LENGTH} characters' in str(context.exception)
        )

    def test_last_name_starts_with_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['last_name'] = 'smith'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertEquals(
            f"{Profile.LAST_NAME_CHECK_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE}", str(context.exception)
        )

    def test_password_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'Pass123!'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(
            'Ensure this value has at least 8 characters' in str(context.exception)
        )

    def test_password_must_have_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'password123!'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(
            'The password must contain at least one uppercase letter' in str(context.exception)
        )

    def test_password_must_have_lowercase_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'PASSWORD123!'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(
            'The password must contain at least one lowercase letter' in str(context.exception)
        )

    def test_password_must_have_special_symbol_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'Password123'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(
            'The password must contain at least one special symbol' in str(context.exception)
        )

    def test_password_must_have_number_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'Password!'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(
            'The password must contain at least one number' in str(context.exception)
        )

    def test_valid_password(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'ValidPass123!'
        profile = Profile.objects.create(**profile_data)
        self.assertTrue(profile.check_password('ValidPass123!'))

    def test_city_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['city'] = 'A' * (Profile.LOCATION_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(f'Ensure this value has at least {Profile.LOCATION_MIN_LENGTH} characters' in str(context.exception))

    def test_city_max_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['city'] = 'A' * (Profile.LOCATION_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(Profile.LOCATION_MAX_LENGTH in str(context.exception))

    def test_city_must_start_with_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['city'] = 'test city'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(Profile.LOCAL_LOCATION_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE in str(context.exception))

    def test_country_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['country'] = 'A' * (Profile.LOCATION_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(f'Ensure this value has at least {Profile.LOCATION_MIN_LENGTH} characters' in str(context.exception))

    def test_country_max_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['country'] = 'A' * (Profile.LOCATION_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(f'Ensure this value has at most {Profile.LOCATION_MAX_LENGTH} characters' in str(context.exception))

    def test_country_must_start_with_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['country'] = 'test country'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue(Profile.COUNTRY_LOCATION_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE in str(context.exception))

    def test_passwords_do_not_match_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password2'] = 'DifferentPassword123!'
        with self.assertRaises(ValidationError) as context:
            Profile.objects.create(**profile_data)

        self.assertTrue('Passwords do not match.' in str(context.exception))

    def test_str_successfully(self):
        profile_data = self.profile_data.copy()
        profile = Profile.objects.create(**profile_data)

        self.assertEquals(str(profile), 'test_user')

    def test_created_successfully(self):
        profile_data = self.profile_data.copy()
        profile = Profile.objects.create(**profile_data)
        self.assertEqual(profile.username, 'test_user')
        self.assertEqual(profile.first_name, 'John')
        self.assertEqual(profile.last_name, 'Doe')
        self.assertEqual(str(profile.birthday), '1990-01-01')
        self.assertEqual(profile.city, 'Test City')
        self.assertEqual(profile.country, 'Test Country')
        self.assertEqual(profile.sex, 'Male')
        self.assertTrue(profile.check_password('Password123!'))
        self.assertEqual(profile.password2, 'Password123!')
