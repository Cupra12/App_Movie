from django import forms
from django.forms import ModelForm
from .models import Movie, Director, Comment



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'author', 'ratings']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Mój komentarz..."}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': 'name', 'id': 'admin', 'type': 'hidden'}),
            'ratings': forms.Select(attrs={'choices': 'RATING_CHOICES', 'class': 'form-control'})
        }



class Directors_Form(ModelForm):
    class Meta:
        model = Director
        fields = ['name_surname', 'birthday', 'director_photo', 'about_director']



class Movie_Form(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'author', 'ang_name', 'description', 'film_director', 'year', 'released', 'photo', 'categories', 'clip_movie']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': "Nazwa Filmu..."}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': 'name', 'id': 'admin', 'type': 'hidden'}),
            'ang_name': forms.TextInput(attrs={'class': 'input', 'placeholder': "Angielska nazwa Filmu..."}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'rows': 10, 'placeholder': "Opis..."}),
            'film_director': forms.Select(attrs={'class': 'form-control', 'placeholder': "Wybierz..."}),

            'year': forms.DateInput(attrs={'class': 'input', 'placeholder': "Premiera światowa..."}),
            'released': forms.DateInput(attrs={'class': 'input', 'placeholder': "Data publikacji..."}),
            'photo': forms.FileInput(attrs={'class': 'input', 'placeholder': "Data publikacji..."}),

            'categories': forms.SelectMultiple(attrs={'class': 'input', 'placeholder': "Wybierz kategorie..."}),
            'clip_movie': forms.FileInput(attrs={'class': 'input', 'placeholder': "Dodaj film..."}),
        }