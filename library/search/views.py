import operator

from django.shortcuts import render
from django.http import HttpResponse
import collections
from goodreads import client
import json

genreExceptions = [
    'to-read', 'currently-reading', 'owned', 'default', 'favorites', 'books-i-own',
    'ebook', 'kindle', 'library', 'audiobook', 'owned-books', 'audiobooks', 'my-books',
    'ebooks', 'to-buy', 'english', 'calibre', 'books', 'british', 'audio', 'my-library',
    'favourites', 're-read', 'general', 'e-books', 'novel',
]

api_key = 'EqndoyFbNOOEy27w5SDCA'
api_secret = 'WDlcyAlmNzIHuzo3Ld66YkXeqUAFCLuKvGmlOpRQ8'


def search(q, page=1, search_field='all', strict=False):
    local_client = client.GoodreadsClient(api_key, api_secret)
    resp = local_client.request("search/index.xml",
                                {'q': q, 'page': page, 'search[field]': search_field})
    works = resp['search']['results']['work']

    if type(works) == collections.OrderedDict:
        works = [works]

    ret = []
    for work in works[0:3]:
        if (strict and work['best_book']['title'].lower() == q) or not strict:
            ret.append(local_client.book(work['best_book']['id']['#text']))

    return ret


def home(request):
    return render(request, 'search/home.html')


def books(request):
    query = request.GET['query']
    data = search(query.lower(), search_field='title', strict=False)
    jsonish = []

    for book in data:
        combauth = ''
        for author in book.authors:
            combauth += author.name + ', '
        genres_txt = ''
        try:
            genre_names = [shelf.name for shelf in book.popular_shelves]
            genres = list(set(genre_names) - set(genreExceptions))
            for genre in genres[:3]:
                genres_txt += genre + ', '
        except:
            print('dead');

        short = {
            'title': book.title,
            'author': combauth[:-2],
            'genre': genres_txt[:-2],
            'small_img': book.small_image_url,
        }
        jsonish.append(short)

    return HttpResponse(json.dumps(jsonish))
    # Sending an success response
