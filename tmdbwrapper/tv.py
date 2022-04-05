# -*- coding: utf-8 -*-
# from . import session
from dotenv import load_dotenv
import os
import requests
from requests.exceptions import HTTPError

load_dotenv()

class APIKeyMissingError(Exception):
    pass

class TV(object):

    def __init__(self):
        self.session = self._get_session()

    def popular(self,page):
        path = f'https://api.themoviedb.org/3/tv/popular'
        self.session.params['page'] = page
        response = self.session.get(path)
        if response.status_code == 200:
            records = response.json()['results']
            return [(r['id'],r['name'],r['original_language'],r['vote_average']) for r in records]
        else:
            raise HTTPError(f'HTTP Error {response.status_code}: {response.reason}')

    def _get_session(self):
        TMDB_API_KEY = os.environ.get('TMDB_API_KEY', None)
        # TMDB_API_KEY = None
        if TMDB_API_KEY is None:
            raise APIKeyMissingError(
                "All methods require an API key. See "
                "https://developers.themoviedb.org/3/getting-started/introduction "
                "for how to retrieve an authentication token from "
                "The Movie Database"
            )
        session = requests.Session()
        session.params = {}
        session.params['api_key'] = os.environ.get('TMDB_API_KEY', None)
        return session

if __name__ == '__main__':
    mytv = TV()
    result = mytv.popular(500)
    print(result)