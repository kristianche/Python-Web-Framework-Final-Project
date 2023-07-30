from django import forms
from .models import Book, Author, Publisher, Profile
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['reviews_counter', 'created_by']
        labels = {
            'title': '',
            'author': '',
            'image_url': '',
            'genre': '',
            'publisher': '',
            'publication_date_book': '',
            'description': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Genre'}),
            'publisher': forms.TextInput(attrs={'placeholder': 'Publisher'}),
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
            'first_name': '',
            'last_name': '',
            'biography': ''
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'biography': forms.Textarea(attrs={'placeholder': 'Biography'})
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
            'name': '',
            'description': '',
            'image_url': '',
            'website': '',
            'email': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'})
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

