from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, Directors_Form, Movie_Form
from .models import Movie, Comment, Category, Director, Like
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect




def HomeView(request):
    return render(request, 'Home.html')



class AllMovies(ListView):
    model = Movie
    template_name = 'All_movies.html'
    paginate_by = 30
    context_object_name = 'movie'

    def get_context_data(self, *args, **kwargs):
        get_dict_copy = self.request.GET.copy()
        get_dict_copy.pop('page', True)
        return super().get_context_data(
            *args,
            **kwargs,
            cat_menu=Category.objects.all(),
            search_term=self.request.GET.get('search', ''),
            params=get_dict_copy.urlencode()
        )
    def get_queryset(self, *args, **kwargs):
        films = super().get_queryset(*args, **kwargs)
        if 'search' in self.request.GET:
            search_term = self.request.GET['search']
            return films.filter(name__icontains=search_term)
        return films



def movie_category(request, category):
    movies = Movie.objects.filter(categories__name__contains=category.replace('-', ''))
    return render(request, "movie_category.html", {"category": category, "movies": movies})



def movie_detail(request, pk):
    postq = Movie.objects.all()
    post = Movie.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    user = request.user
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                ratings=form.cleaned_data["ratings"],
                post=post,
            )
            comment.save()
    return render(request, "movie_detail.html", {"post": post, "comments": comments, "form": form, "user": user, "postq": postq})



def TopTen(request):
    movies = Movie.objects.all()
    comments = Comment.objects.filter(ratings=10)
    user = request.user
    context = {
        'movies': movies,
        'comments': comments,
        'user': user,
    }
    return render(request, 'TopTen.html', context)



def Delete_comment(request, id):
    obj = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('AllMovies')
    return render(request, "Delete_comment.html", {"object": obj})



def AllDirectors(request):
    director = Director.objects.all()
    search_director = ''
    if 'search' in request.GET:
        search_director = request.GET['search']
        director = director.filter(name_surname__icontains=search_director)
    paginator = Paginator(director, 30)
    page = request.GET.get('page')
    director = paginator.get_page('page')

    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    return render(request, 'AllDirectors.html', {'director': director, 'search_director': search_director, 'params': params})



def DirectorsDetail(request, id):
    director = get_object_or_404(Director, pk=id)
    return render(request, 'DirectorsDetail.html', {'director': director})



def New_Directors(request):
    if request.method == 'POST':
        form = Directors_Form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, f'Reżyser został dodany!')
            return redirect('AllDirectors')
    else:
        form = Directors_Form()
    return render(request, 'New_Directors.html', {'form': form})



def Edit_Movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    form = Movie_Form(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('AllMovies')
    return render(request, 'New_Movie.html', {'form': form})



def New_Movie(request):
    if request.method == 'POST':
        form = Movie_Form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, f'Film został dodany!')
            return redirect('AllMovies')
    else:
        form = Movie_Form()
    return render(request, 'New_Movie.html', {'form': form})



def Delete_Movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('AllMovies')
    return render(request, 'Delete_Movie.html', {'movie': movie})



def Edit_Directors(request, id):
    director = get_object_or_404(Director, pk=id)
    form = Directors_Form(request.POST or None, request.FILES or None, instance=director)
    if form.is_valid():
        form.save()
        return redirect('AllDirectors')
    return render(request, 'New_Directors.html', {'form': form})



def Delete_Directors(request, id):
    director = get_object_or_404(Director, pk=id)
    if request.method == 'POST':
        director.delete()
        return redirect('AllDirectors')
    return render(request, 'Delete_Directors.html', {'director': director})



def LikeView(request, pk):
    user = request.user
    if request.method == 'POST':
        poster_id = request.POST.get('movie_id')
        movie_obj = Movie.objects.get(pk=str(pk))
        if user in movie_obj.likes.all():
            movie_obj.likes.remove(user)
        else:
            movie_obj.likes.add(user)
        like, created = Like.objects.get_or_create(user=user, poster_id=str(pk))
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return HttpResponseRedirect(reverse('movie_detail', args=[str(pk)]))

