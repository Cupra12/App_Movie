from django.urls import path
from . import views
from.views import HomeView, AllMovies, LikeView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.HomeView, name='Home'),

    path("AllMovies/", AllMovies.as_view(), name="AllMovies"),
    path('AllDirectors/', views.AllDirectors, name='AllDirectors'),
    path("TopTen/", views.TopTen, name='TopTen'),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    path('add/movie/', views.New_Movie, name='New_Movie'),
    path('edit/<int:id>/', views.Edit_Movie, name='Edit_Movie'),
    path('delete/<int:id>/', views.Delete_Movie, name='Delete_Movie'),
    path('moreDirectors/<int:id>/', views.DirectorsDetail, name='DirectorsDetail'),
    path('add/directors/', views.New_Directors, name='New_Directors'),
    path('edit/directors/<int:id>/', views.Edit_Directors, name='Edit_Directors'),
    path('delete/directors/<int:id>/', views.Delete_Directors, name='Delete_Directors'),
    path("delete/comment/<int:id>/", views.Delete_comment, name="Delete_comment"),
    path("category/<str:category>/", views.movie_category, name="category"),
    path("like/<int:pk>/", LikeView, name="like_movie"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
