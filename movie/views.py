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
            page_num = int(s[index + 1])
            break
    movies = Movie.objects.all()
    movie_list = []
    for item in movies:
        movie_list.append(item)
    page = len(movies) // 10
    if (len(movies) / 10 - len(movies) // 10) > 0:
        page += 1
    pages = []
    for index in range(page):
        pages.append(index + 1)
    result = movie_list[10 * (page_num - 1):10 * page_num]
    data = {'items': result, 'number': len(movies), 'pages': pages, 'current_page': page_num, 'next_page': page_num + 1,
            'last_page': page_num - 1, 'page_number': page}
    if page_num == 1:
        del data['last_page']
    if page_num == page:
        del data['next_page']

    return render(request, 'movie_list.html', data)


def actor_all(request):
    s = str(request.get_raw_uri()).split('/')
    for index in range(len(s)):
        if s[index] == 'actor_all':
            page_num = int(s[index + 1])
            break
    actors = Actor.objects.all()
    actor_list = []
    for item in actors:
        actor_list.append(item)
    page = len(actors) // 10
    if (len(actors) / 10 - len(actors) // 10) > 0:
        page += 1
    pages = []
    for index in range(page):
        pages.append(index + 1)
    result = actor_list[10 * (page_num - 1):10 * page_num]
    data = {'items': result, 'number': len(actors), 'pages': pages, 'current_page': page_num, 'next_page': page_num + 1,
            'last_page': page_num - 1, 'page_number': page}
    if page_num == 1:
        del data['last_page']
    if page_num == page:
        del data['next_page']
    return render(request, 'actor_list.html', data)


def movie_search(request):
    s = str(request.get_raw_uri()).split('/')
    for index in range(len(s)):
        if s[index] == 'movie_search':
            pattern = s[index + 1]
            break
    pattern = pattern.replace("%20", " ")
    movies = Movie.objects.filter(title__contains=pattern)
    return render(request, 'movie_list.html', {'items': movies, 'search': pattern, 'number': len(movies)})


def actor_search(request):
    print(request)
    s = str(request.get_raw_uri()).split('/')
    for index in range(len(s)):
        if s[index] == 'actor_search':
            pattern = s[index + 1]
            break
    pattern = pattern.replace("%20", " ")
    print(pattern)
    actors = Actor.objects.filter(name__contains=pattern)
    return render(request, 'actor_list.html', {'items': actors, 'search': pattern, 'number': len(actors)})


def search(request):

    s = str(request.get_raw_uri()).split('/')
    for index in range(len(s)):
        if s[index] == 'search':
            pattern = s[index + 1]
            break
    pattern = pattern.replace("%20", " ")
    movies = Movie.objects.filter(title__contains=pattern)
    actors = Actor.objects.filter(name__contains=pattern)
    return render(request, 'searchresult.html', {'items1': movies, 'search1': pattern, 'number1': len(movies), 'items2': actors, 'search2': pattern, 'number2': len(actors)})


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
