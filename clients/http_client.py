import requests
from superheroes.settings import URL


class HttpClient:

    def get_heroes_list_page(self, path="/ids.html"):
        response = requests.get(f'{URL}{path}')
        response.raise_for_status()
        return response
