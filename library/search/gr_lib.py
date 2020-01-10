import collections

from goodreads import client
from time import time

api_key = 'EqndoyFbNOOEy27w5SDCA'
api_secret = 'WDlcyAlmNzIHuzo3Ld66YkXeqUAFCLuKvGmlOpRQ8'


def search(local_client, q, page=1, search_field='all', strict=False):
    resp = local_client.request("search/index.xml",
                                {'q': q, 'page': page, 'search[field]': search_field})
    works = resp['search']['results']['work']

    if type(works) == collections.OrderedDict:
        works = [works]

    ret = []
    for work in works[0:5]:
        if (strict and work['best_book']['title'].lower() == q) or not strict:
            ret.append(local_client.book(work['best_book']['id']['#text']))

    return ret


gc = client.GoodreadsClient(api_key, api_secret)
