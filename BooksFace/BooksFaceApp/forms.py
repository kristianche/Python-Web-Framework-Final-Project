from django import forms
from .models import Book, Author, Publisher, Profile
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm


class PlaceholderSelect(forms.Select):
    def __init__(self, attrs=None, choices=(), empty_label=None):
        super().__init__(attrs, choices)
        self.empty_label = empty_label

    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if 'index' in option and option['index'] == 0 and self.empty_label:
            option['label'] = self.empty_label
        return option


class BookCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].widget.attrs['placeholder'] = 'Genre'

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

        empty_label = 'Select a genre'


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


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')
        labels = {
            'username': '',
            'email': '',
            'first_name': '',
            'last_name': '',
            'password': '',
            'password2': ''
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'})
        }

        help_texts = {
            'username': '',
            'password': '',
        }


class ProfileEditForm(ProfileCreateForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(ProfileCreateForm):
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


