from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Director(models.Model):
    name_surname = models.CharField(max_length=100, unique=True)
    director_photo = models.ImageField(upload_to='other/author_image_user/', blank=True, null=True, default='films_image/domyslny.jpg')
    birthday = models.DateField(null=True, blank=True)
    about_director = models.TextField(default="")

    def __str__(self):
        return self.name_surname
    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Director"



class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"


RATING_CHOICES = [
        (1, '1 - Śmieć'),
        (2, '2 - Straszne słaby'),
        (3, '3 - Słaby'),
        (4, '4 - Zły'),
        (5, '5 - OK'),
        (6, '6 - Oglądalny'),
        (7, '7 - Dobry'),
        (8, '8 - Bardzo dobry'),
        (9, '9 - Perfekcyjny'),
        (10, '10 - Arcydzieło'),
    ]


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ang_name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    film_director = models.ForeignKey(Director, on_delete=models.CASCADE)
    year = models.IntegerField(null=True, blank=True)  # null pole wymagane true / false
    released = models.DateField(null=True, blank=True)  # wypuszczony(produkcja) filmu
    photo = models.ImageField(null=True, blank=True, upload_to='other/image_user/', default='films_image/domyslny.jpg')
    categories = models.ManyToManyField("Category", related_name="posts")
    clip_movie = models.FileField(null=True, blank=True, upload_to='other/videos_user/', default='videos/videoplayback.mp4')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "movie"
        verbose_name_plural = "movie"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # models.ForeignKey(User, on_delete=models.CASCADE)  /models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("movie", on_delete=models.CASCADE)
    ratings = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)


    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comment"


class TopTen(models.Model):
    post = models.ForeignKey("movie", on_delete=models.CASCADE)
    ratings = models.ForeignKey("comment", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(auto_now_add=True,  null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.post)

    class Meta:
        verbose_name = "TopTen"
        verbose_name_plural = "TopTen"