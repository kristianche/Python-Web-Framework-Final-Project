from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError
from BooksFace.BooksFaceApp.models import Profile
from BooksFace.BooksFaceApp.validators import (
    check_password_capital_letter,
    check_password_lowercase_letter,
    check_password_special_symbol,
    check_password_number
)


class ProfileModelTest(TestCase):
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

    def test_first_name_max_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['first_name'] = 'A' * (Profile.NAMES_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

    def test_first_name_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['first_name'] = 'A' * (Profile.NAMES_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError):
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

    def test_first_name_starts_with_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['first_name'] = 'john'
        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

        self.assertEquals(
            f"{Profile.FIRST_NAME_CHECK_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE}", str(context.exception.messages[0])
        )

    def test_last_name_max_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['last_name'] = 'A' * (Profile.NAMES_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

    def test_last_name_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['last_name'] = 'A' * (Profile.NAMES_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError):
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

    def test_last_name_starts_with_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['last_name'] = 'smith'
        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

        self.assertEquals(
            f"{Profile.LAST_NAME_CHECK_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE}", str(context.exception.messages[1])
        )

    def test_password_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'Pass123!'
        with self.assertRaises(ValidationError):
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

    def test_password_must_have_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = "abc@1234"
        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

        self.assertEquals("Password must contain at least one capital letter!", str(context.exception.messages[2]))

    def test_password_must_have_lowercase_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'PASSWORD123!'
        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

        self.assertEquals(
            'Password must contain at least one lowercase letter!', str(context.exception.messages[3])
        )

    def test_password_must_have_special_symbol_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'Password123'
        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

        self.assertEquals(
            'Password must contain at least one special symbol!', str(context.exception.messages[4])
        )

    def test_password_must_have_number_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password'] = 'Password!'
        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

        self.assertEquals(
            'Password must contain at least one number!', str(context.exception.messages[5])
        )

    def test_city_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['city'] = 'A' * (Profile.LOCATION_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError):
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

    def test_city_max_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['city'] = 'A' * (Profile.LOCATION_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

    def test_city_must_start_with_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['city'] = 'test city'
        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

        self.assertTrue(Profile.LOCAL_LOCATION_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE in str(context.exception))

    def test_country_min_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['country'] = 'A' * (Profile.LOCATION_MIN_LENGTH - 1)
        with self.assertRaises(ValidationError):
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

    def test_country_max_length_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['country'] = 'A' * (Profile.LOCATION_MAX_LENGTH + 1)
        with self.assertRaises(ValidationError):
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

    def test_country_must_start_with_capital_letter_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['country'] = 'test country'
        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(**profile_data)
            profile.full_clean()

        self.assertTrue(Profile.COUNTRY_LOCATION_STARTS_WITH_CAPITAL_LETTER_ERROR_MESSAGE in str(context.exception))

    def test_passwords_do_not_match_raises_error(self):
        profile_data = self.profile_data.copy()
        profile_data['password2'] = 'DifferentPassword123!'
        with self.assertRaises(ValidationError) as context:
            profile = Profile.objects.create(**profile_data)
            profile.clean()

        self.assertEquals(str(context.exception.messages[0]), "Passwords do not match.")

    def test_str_successfully(self):
        profile_data = self.profile_data.copy()
        profile = Profile.objects.create(**profile_data)

        self.assertEquals(str(profile), 'test_user')

    def test_created_successfully(self):
        profile_data = self.profile_data.copy()
        profile = Profile.objects.create(**profile_data)
        self.assertEquals(profile.username, 'test_user')
        self.assertEquals(profile.first_name, 'John')
        self.assertEquals(profile.last_name, 'Doe')
        self.assertEquals(str(profile.birthday), '1990-01-01')
        self.assertEquals(profile.city, 'Test City')
        self.assertEquals(profile.country, 'Test Country')
        self.assertEquals(profile.sex, 'Male')
        self.assertEquals(profile.password, 'Password123!')
        self.assertEquals(profile.password2, 'Password123!')
