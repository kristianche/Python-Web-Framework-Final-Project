from django.urls import path, include
from. import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home-page'),
    path('authors/', include([
        path('', views.Authors.as_view(), name='authors-display'),
        path('author/', include([
            path('<int:pk>/', include([
                path('', views.AuthorDetails.as_view(), name='author-details'),
                path('edit/', views.AuthorEdit.as_view(), name='author-edit'),
                path('delete/', views.AuthorDelete.as_view(), name='author-delete')
            ])),
            path('create/', views.AuthorCreate.as_view(), name='author-create'),
        ]))
    ])),
    path('books/', include([
        path('', views.Books.as_view(), name='books-display'),
        path('book/', include([
            path('<int:pk>/', include([
                path('', views.BookDetails.as_view(), name='book-details'),
                path('edit/', views.BookEdit.as_view(), name='book-edit'),
                path('delete/', views.BookDelete.as_view(), name='book-delete')
            ])),
            path('create/', views.BookCreate.as_view(), name='book-create'),

        ]))
    ])),
    path('publishers/', include([
        path('', views.Publishers.as_view(), name='publishers-display'),
        path('publisher/', include([
            path('<int:pk>/', include([
                path('', views.PublisherDetails.as_view(), name='publisher-details'),
                path('edit/', views.PublisherEdit.as_view(), name='publisher-edit'),
                path('delete/', views.PublisherDelete.as_view(), name='publisher-delete')
            ])),
            path('create/', views.PublisherCreate.as_view(), name='publisher-create'),

        ])),
    ])),
    path('profile/', include([
        path('<int:pk>', include([
            path('', views.ProfileDetails.as_view(), name='profile-details'),
            path('edit/', views.ProfileEdit.as_view(), name='profile-edit'),
            path('edit/', views.ProfileDelete.as_view(), name='profile-delete')
        ])),
        path('create/', views.ProfileCreate.as_view(), name='profile-create')
    ])),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout')
]