from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import BookSearchForm, AuthorSearchForm, PublisherSearchForm, ReviewCreationForm, ReviewEditForm, \
    ReviewDeleteForm
from .models import Book, Author, Publisher, Profile, ReviewBook
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        book = Book.objects.get(pk=pk)
        reviews = ReviewBook.objects.filter(book=book)
        average_grade = 0
        if reviews:
            counter = 0
            for review in reviews:
                counter += 1
                average_grade += review.grade
            average_grade = round(average_grade / counter, 1)
        context['average_grade'] = average_grade
        return context


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
        title = form.cleaned_data['title']
        if Book.objects.filter(title=title).exists():
            form.add_error('title', 'A book with this title already exists.')
            return self.form_invalid(form)

        form.instance.created_by = self.request.user.username

        return super().form_valid(form)


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
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        if Author.objects.filter(first_name=first_name, last_name=last_name).exists():
            form.add_error(None, 'An author with this name already exists.')
            return self.form_invalid(form)

        form.instance.created_by = self.request.user.username

        return super().form_valid(form)


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
    success_url = reverse_lazy('publishers-display')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        if Publisher.objects.filter(name=name).exists():
            form.add_error('name', 'A publisher with this name already exists.')
            return self.form_invalid(form)

        form.instance.created_by = self.request.user.username
        return super().form_valid(form)


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


def profile_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = Profile.objects.get(user=user)

    context = {
        'profile': profile
    }

    return render(request, template_name='profile/profile-details.html', context=context)


class ProfileCreate(generic.CreateView):
    model = Profile
    form_class = forms.ProfileCreateForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        profile, created = Profile.objects.get_or_create(
            user=self.object,
            defaults={
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name']
            }
        )

        if not created:
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.save()
        
        return result


class ProfileEdit(generic.UpdateView, LoginRequiredMixin):
    model = Profile
    form_class = forms.ProfileEditForm
    template_name = 'profile/profile-edit.html'

    def get_success_url(self):

        return reverse_lazy('profile-details', args=[self.object.user.pk])


@login_required()
def profile_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        logout(request)
        profile.delete()
        user.delete()
        return redirect('home-page')

    context = {
        'user': user,
    }

    return render(request, template_name='profile/profile-delete.html', context=context)


class Logout(auth_views.LogoutView, LoginRequiredMixin):
    success_url = reverse_lazy('home-page')


class Login(auth_views.LoginView):
    template_name = 'common/login.html'
    success_url = reverse_lazy('home-page')
    redirect_authenticated_user = True


def books_by_author(request, pk):
    author = Author.objects.filter(pk=pk).get()
    books = Book.objects.filter(author=author)

    context = {
        'books': books,
        'author': author
    }

    return render(request, template_name='books/books-by-author.html', context=context)


def books_by_publisher(request, pk):
    publisher = Publisher.objects.filter(pk=pk).get()
    books = Book.objects.filter(publisher=publisher)

    context = {
        'books': books,
        'publisher': publisher
    }

    return render(request, template_name='books/books-by-publisher.html', context=context)


@login_required()
def review_creation(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = ReviewCreationForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user.username
            review.book = book
            book.reviews_counter_increase()
            book.save()
            review.save()
            return redirect('books-display')

    else:
        form = ReviewCreationForm()

    context = {
        'form': form,
        'book': book
    }

    return render(request, template_name='reviews/review-create.html', context=context)


def view_book_reviews(request, pk):
    book = Book.objects.get(pk=pk)
    reviews = ReviewBook.objects.filter(book=book).order_by('-review_date')

    context = {
        'reviews': reviews,
        'book': book
    }

    return render(request, template_name='reviews/reviews-book-display.html', context=context)


@login_required()
def review_edit(request, pk):
    review = get_object_or_404(ReviewBook, pk=pk)

    if request.method == 'POST':
        form = ReviewEditForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('books-display')
    else:
        form = ReviewEditForm(instance=review)

    context = {
        'form': form,
        'review': review
    }

    return render(request, template_name='reviews/review-edit.html', context=context)


@login_required()
def review_delete(request, pk):
    review = get_object_or_404(ReviewBook, pk=pk)
    book = Book.objects.get(title=review.book.title)

    if request.method == 'POST':
        form = ReviewDeleteForm(request.POST, instance=review)
        if form.is_valid():
            book.reviews_counter -= 1
            book.save()
            review.delete()
            return redirect('books-display')
    else:
        form = ReviewDeleteForm(instance=review)

    context = {
        'form': form,
        'review': review
    }

    return render(request, template_name='reviews/review-delete.html', context=context)
