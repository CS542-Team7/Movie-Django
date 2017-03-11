from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from movie.models import *


@csrf_protect
def movie_detail(request):
    s = str(request.get_raw_uri()).split('/')
    for index in range(len(s)):
        if s[index] == 'movie_detail':
            movie_id = s[index + 1]
            break

    if request.POST:
        history = Favorite.objects.filter(movieid_id=movie_id, username=request.user.get_username())
        if len(history) == 0:
            new_record = Favorite(movieid_id=movie_id, username=request.user.get_username())
            new_record.save()

    try:
        movie = Movie.objects.get(movieid=movie_id)
    except:
        return render(request, '404.html')
    records = Act.objects.filter(movieid_id=movie_id)
    actors = []
    for query in records:
        for actor in Actor.objects.filter(actorid=query.actorid_id):
            actors.append(actor)
    return render(request, 'actor_list.html', {'items': actors, 'number': len(actors), 'movie': movie})


def actor_detail(request):
    s = str(request.get_raw_uri()).split('/')
    for index in range(len(s)):
        if s[index] == 'actor_detail':
            actor_id = s[index + 1]
            break
    try:
        actor = Actor.objects.get(actorid=actor_id)
    except:
        return render(request, '404.html')
    records = Act.objects.filter(actorid_id=actor_id)
    movies = []
    for query in records:
        for movie in Movie.objects.filter(movieid=query.movieid_id):
            movies.append(movie)
    return render(request, 'movie_list.html', {'items': movies, 'number': len(movies), 'actor': actor})


def movie_all(request):
    s = str(request.get_raw_uri()).split('/')
    for index in range(len(s)):
        if s[index] == 'movie_all':
            num = s[index + 1]
            break
    movies = Movie.objects.all()
    list = []
    for item in movies:
        list.append(item)
    print(list)
    page = len(movies) // 10
    if (len(movies) / 10 - len(movies) // 10) > 0:
        page += 1
    pages = []
    for index in range(page):
        pages.append(index + 1)
    print(pages)
    result = []
    num = int(num)
    for index in range(len(list)):
        if index >= (num - 1) * 10:
            result.append(list[index])
        if index > num * 10:
            break
    return render(request, 'movie_list.html', {'items': result, 'number': len(movies), 'pages': pages})


def actor_all(request):
    actors = Actor.objects.all()
    return render(request, 'actor_list.html', {'items': actors, 'number': len(actors)})


def movie_search(request):
    s = str(request.get_raw_uri()).split('/')
    for index in range(len(s)):
        if s[index] == 'movie_search':
            pattern = s[index + 1]
            break
    pattern = pattern.replace("%20", " ")
    print(pattern)
    movies = Movie.objects.filter(title__contains=pattern)
    return render(request, 'movie_list.html', {'items': movies, 'search': pattern, 'number': len(movies)})


def actor_search(request):
    s = str(request.get_raw_uri()).split('/')
    for index in range(len(s)):
        if s[index] == 'actor_search':
            pattern = s[index + 1]
            break
    actors = Actor.objects.filter(name__contains=pattern)
    return render(request, 'actor_list.html', {'items': actors, 'search': pattern, 'number': len(actors)})


@csrf_protect
def favorite(request):
    if request.POST:
        s = str(request.get_raw_uri()).split('/')
        for index in range(len(s)):
            if s[index] == 'favorite':
                movie_id = s[index + 1]
                break
        d = Favorite.objects.get(username=request.user.get_username(), movieid_id=movie_id)
        d.delete()
    records = Favorite.objects.filter(username=request.user.get_username())
    movies = []
    for record in records:
        movie_id = str(record).split('|')[1]
        movies.append(Movie.objects.get(movieid=movie_id))
    return render(request, 'favorite.html', {'items': movies, 'number': len(movies)})
