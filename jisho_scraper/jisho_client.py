# Reference:
# https://jisho.org/forum/54fefc1f6e73340b1f160000-is-there-any-kind-of-search-api

from typing import List

import requests

from jisho_scraper.jisho_data import WordData, Japanese, Sense, Link, Source

BASE_URL = 'https://jisho.org/api/v1'
WORD_SEARCH_ENDPOINT = '/search/words'

MAX_PAGES = 10


def search_word(keyword):
    page = 1
    rv = []

    while page <= MAX_PAGES:
        current_page_data = __search_word_page(keyword, page)
        if current_page_data:
            rv += current_page_data
        else:
            break
        page += 1

    return rv


def __search_word_page(keyword: str, page: int) -> List[WordData]:
    payload = {'keyword': keyword, 'page': page}
    r = requests.get(f'{BASE_URL}{WORD_SEARCH_ENDPOINT}', params=payload)
    r.raise_for_status()

    data = r.json()['data']
    data = [__process_word_data(x) for x in data]
    return data


def __process_word_data(d: dict) -> WordData:
    d['japanese'] = [__process_japanese(x) for x in d['japanese']]
    d['senses'] = [__process_sense(x) for x in d['senses']]
    return WordData(**d)


def __process_japanese(d: dict) -> Japanese:
    return Japanese(**d)


def __process_sense(d: dict) -> Sense:
    d['links'] = [__process_link(x) for x in d['links']]
    d['source'] = [__process_source(x) for x in d['source']]
    return Sense(**d)


def __process_link(d: dict) -> Link:
    return Link(**d)


def __process_source(d: dict) -> Source:
    return Source(**d)
