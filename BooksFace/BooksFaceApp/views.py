from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import BookSearchForm, AuthorSearchForm, PublisherSearchForm
from .models import Book, Author, Publisher, Profile
from . import forms
from django.contrib.auth import views as auth_views


class IndexView(generic.TemplateView):
    template_name = 'common/index.html'


class Books(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books-display.html'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        if query:
            return Book.objects.filter(title__icontains=query)
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = BookSearchForm()
        context['button_title'] = 'Create Book'
        return context


class BookDetails(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book-details.html'


class BookCreate(generic.CreateView, LoginRequiredMixin):
    model = Book
    form_class = forms.BookCreateForm
    template_name = 'books/book-create.html'
    success_url = reverse_lazy('books-display')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        authors = Author.objects.all()
        context['authors'] = authors
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        title = form['title']
        if not book_exists(title):
            Book.created_by = self.request.user
            return result
        else:
            raise ValidationError(f'There is already created a book with name {title}.')


class BookEdit(generic.UpdateView, LoginRequiredMixin):
    model = Book
    form_class = forms.BookEditForm
    template_name = 'books/book-edit.html'

    def get_success_url(self):

        return reverse_lazy('book-details', args=[self.object.pk])


class BookDelete(generic.DeleteView, LoginRequiredMixin):
    model = Book
    form_class = forms.BookDeleteForm
    template_name = 'books/book-delete.html'
    success_url = reverse_lazy('books-display')

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs


class Authors(generic.ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'author/authors-display.html'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        if query:
            return Author.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
        return Author.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = AuthorSearchForm()
        context['button_title'] = 'Create Author'
        return context


class AuthorDetails(generic.DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'author/author-details.html'


class AuthorCreate(generic.CreateView, LoginRequiredMixin):
    model = Author
    form_class = forms.AuthorCreateForm
    template_name = 'author/author-create.html'
    success_url = reverse_lazy('authors-display')

    def form_valid(self, form):
        result = super().form_valid(form)

        Author.created_by = self.request.user

        return result


class AuthorEdit(generic.UpdateView, LoginRequiredMixin):
    model = Author
    form_class = forms.AuthorEditForm
    template_name = 'author/author-edit.html'

    def get_success_url(self):

        return reverse_lazy('author-details', args=[self.object.pk])


class AuthorDelete(generic.DeleteView, LoginRequiredMixin):
    model = Author
    form_class = forms.AuthorDeleteForm
    template_name = 'author/author-delete.html'
    success_url = reverse_lazy('authors-display')

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs


class Publishers(generic.ListView):
    model = Publisher
    context_object_name = 'publishers'
    template_name = 'publisher/publishers-display.html'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        if query:
            return Publisher.objects.filter(name__icontains=query)
        return Publisher.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = PublisherSearchForm()
        context['button_title'] = 'Create Publisher'
        return context


class PublisherDetails(generic.DetailView):
    model = Publisher
    context_object_name = 'publisher'
    template_name = 'publisher/publisher-details.html'


class PublisherCreate(generic.CreateView, LoginRequiredMixin):
    model = Publisher
    form_class = forms.PublisherCreateForm
    template_name = 'publisher/publisher-create.html'
    success_url = reverse_lazy('publisher-create')

    def form_valid(self, form):
        result = super().form_valid(form)

        Publisher.created_by = self.request.user

        return result


class PublisherEdit(generic.UpdateView, LoginRequiredMixin):
    model = Publisher
    form_class = forms.PublisherEditForm
    template_name = 'publisher/publisher-edit.html'

    def get_success_url(self):

        return reverse_lazy('publisher-details', args=[self.object.pk])


class PublisherDelete(generic.DeleteView, LoginRequiredMixin):
    model = Publisher
    form_class = forms.PublisherDeleteForm
    template_name = 'publisher/publisher-delete.html'
    success_url = reverse_lazy('publisher-delete')

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs


class ProfileDetails(generic.DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile/profile-details.html'


class ProfileCreate(generic.CreateView):
    model = Profile
    form_class = forms.ProfileCreateForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        
        return result


class ProfileEdit(generic.UpdateView):
    model = Profile
    form_class = forms.ProfileEditForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile-details')


class ProfileDelete(generic.DeleteView):
    model = Profile
    form_class = forms.ProfileDeleteForm
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home-page')


class Logout(auth_views.LogoutView, LoginRequiredMixin):
    success_url = reverse_lazy('home-page')


class Login(auth_views.LoginView):
    template_name = 'common/login.html'
    success_url = reverse_lazy('home-page')
    redirect_authenticated_user = True


class ReviewCreate(generic.CreateView):
    pass



def book_exists(title):
    # Use the 'filter' method to check if the book with the given title exists
    book_queryset = Book.objects.filter(title=title)

    # Check if any book with the given title exists
    return book_queryset.exists()