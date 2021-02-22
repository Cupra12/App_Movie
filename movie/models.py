from django.db import models
from django.contrib.auth.models import User



class Director(models.Model):
    name_surname = models.CharField(max_length=100, unique=True)
    director_photo = models.ImageField(upload_to='other/author_image/', blank=True, null=True, default='films_image/domyslny.jpg')
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
    photo = models.ImageField(null=True, blank=True, upload_to='other/image_movie/', default='films_image/domyslny.jpg')
    categories = models.ManyToManyField("Category", related_name="posts")
    clip_movie = models.FileField(null=True, blank=True, upload_to='other/videos_movie/', default='videos/videoplayback.mp4')
    likes = models.ManyToManyField(User, related_name='like_page')

    @property
    def total_likes(self):
        return self.likes.all().count()

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

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poster = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.poster)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Like"