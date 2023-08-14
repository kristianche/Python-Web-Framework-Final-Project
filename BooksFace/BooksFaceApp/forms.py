from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Book, Author, Publisher, Profile, ReviewBook
from django.contrib.auth.forms import UserCreationForm


class BookCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = 'Author'
        self.fields['genre'].empty_label = 'Genre'
        self.fields['publisher'].empty_label = 'Publisher'

    class Meta:
        model = Book
        exclude = ['reviews_counter', 'created_by', 'likes']
        labels = {
            'title': '',
            'author': '',
            'image': '',
            'genre': '',
            'publisher': '',
            'publication_date_book': '',
            'description': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'author': forms.Select(attrs={'placeholder': 'Author'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'genre': forms.Select(choices=Book.GENRE_CHOICES, attrs={'placeholder': 'Genre'}),
            'publisher': forms.Select(attrs={'placeholder': 'Publisher'}),
            'publication_date_book': forms.DateInput(attrs={'placeholder': 'Book Publication Date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'})
        }


class BookEditForm(BookCreateForm):
    pass


class BookDeleteForm(BookCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['created_by']
        labels = {
            'image': '',
            'first_name': '',
            'last_name': '',
            'biography': '',
            'city': '',
            'country': '',
            'birthday': '',
            'dead': '',
            'nationality': '',
            'nickname': ''
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'biography': forms.Textarea(attrs={'placeholder': 'Biography'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'birthday': forms.DateInput(attrs={'placeholder': 'Birthday'}),
            'dead': forms.DateInput(attrs={'placeholder': 'Died on'}),
            'nickname': forms.TextInput(attrs={'placeholder': 'Nickname'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'}),
            'city': forms.TextInput(attrs={'placeholder': 'Birth City'}),
            'country': forms.TextInput(attrs={'placeholder': 'Birth Country'})
        }


class AuthorEditForm(AuthorCreateForm):
    pass


class AuthorDeleteForm(AuthorCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        exclude = ['created_by']
        labels = {
            'image': '',
            'name': '',
            'description': '',
            'image_url': '',
            'website': '',
            'email': '',
            'office': '',
            'ceo': '',
            'closed': '',
            'founded': ''
        }

        widgets = {
            'image': forms.URLInput(attrs={'placeholder': 'Image'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'founded': forms.TextInput(attrs={'placeholder': 'Founded on'}),
            'office': forms.TextInput(attrs={'placeholder': 'Office'}),
            'ceo': forms.TextInput(attrs={'placeholder': 'CEO'}),
            'closed': forms.TextInput(attrs={'placeholder': 'Closed on'})
        }


class PublisherEditForm(PublisherCreateForm):
    pass


class PublisherDeleteForm(PublisherCreateForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class ProfileCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'username': '',
            'email': '',
            'first_name': '',
            'last_name': '',
            'password1': '',
            'password2': ''
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'})
        }

        help_texts = {
            'username': '',
            'password1': '',
            'password2': ''
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise ValidationError('This email is already taken.')
        return email


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )

        labels = {
            'first_name': '',
            'last_name': '',
            'profile_image': '',
            'city': '',
            'country': '',
            'about_me': '',
            'sex': '',
            'birthday': ''
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'profile_image': forms.URLInput(attrs={'placeholder': 'Image Url'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'city': forms.TextInput(attrs={'placeholder': 'City/Town/Village'}),
            'birthday': forms.DateInput(attrs={'placeholder': 'Birthday'}),
            'about_me': forms.Textarea(attrs={'placeholder': 'About Me'}),
            'sex': forms.Select(attrs={'placeholder': 'Sex'})
        }


class ProfileDeleteForm(ProfileCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class ReviewCreationForm(forms.ModelForm):
    class Meta:
        model = ReviewBook
        exclude = ['likes', 'author', 'book']

        labels = {
            'review': '',
            'book': '',
            'grade': '',
        }

        widgets = {
            'review': forms.Textarea(attrs={'cols': 30, 'rows': 20, 'placeholder': 'Review'}),
            'grade': forms.NumberInput(attrs={'placeholder': 'Book Grade out of 10'}),
            'book': forms.Select(attrs={'disabled': 'disabled'})
        }


class ReviewEditForm(ReviewCreationForm):
    pass


class ReviewDeleteForm(ReviewCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class BookSearchForm(forms.Form):
    search_query = forms.CharField(
        label='',
        max_length=Book.BOOK_TITLE_MAX_LENGTH,
        widget=forms.TextInput(attrs={'placeholder': 'Search Book'})
    )


class AuthorSearchForm(forms.Form):
    search_query = forms.CharField(
        label='',
        max_length=Author.AUTHOR_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={'placeholder': 'Search Author'})
    )


class PublisherSearchForm(forms.Form):
    search_query = forms.CharField(
        label='',
        max_length=Publisher.PUBLISHER_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={'placeholder': 'Search Publisher'})
    )
