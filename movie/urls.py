from django.urls import path
from . import views
from.views import HomeView, AllMovies
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.HomeView, name='Home'),

    path("AllMovies/", AllMovies.as_view(), name="AllMovies"),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    path('add/movie/', views.New_Movie, name='New_Movie'),                               #FilmY
    path('edit/<int:id>/', views.Edit_Movie, name='Edit_Movie'),
    path('delete/<int:id>/', views.Delete_Movie, name='Delete_Movie'),

    path("TopTen/", views.TopTen, name='TopTen'),

    path('AllDirectors/', views.AllDirectors, name='AllDirectors'),
    path('moreDirectors/<int:id>/', views.DirectorsDetail, name='DirectorsDetail'),      #Reżyserowie
    path('add/directors/', views.New_Directors, name='New_Directors'),
    path('edit/directors/<int:id>/', views.Edit_Directors, name='Edit_Directors'),
    path('delete/directors/<int:id>/', views.Delete_Directors, name='Delete_Directors'),

    path("delete/comment/<int:id>/", views.Delete_comment, name="Delete_comment"),      #Komentazrze

    path("category/<str:category>/", views.movie_category, name="category"),            #Gatunki

    path("Testowa_Strona/", views.Testowa_Strona, name='Testowa_Strona'),
    path("Testowa_Strona2/", views.Testowa_Strona2, name='Testowa_Strona2'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
