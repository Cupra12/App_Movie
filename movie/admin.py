from django.contrib import admin
from .models import Movie, Category, Director, Comment, TopTen


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'released')
    list_filter = ('year', 'released')
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post')
    list_filter = ('created_on',)
    search_fields = ('author', 'post')



@admin.register(Director)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'birthday', 'about_director')
    list_filter = ('birthday',)
    search_fields = ('name_surname', 'about_director')



@admin.register(TopTen)
class MovieRatingAdmin(admin.ModelAdmin):
    list_display = ('post', )
    list_filter = ('ratings',)
    search_fields = ('post',)

