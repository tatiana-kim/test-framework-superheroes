import requests
from superheroes.settings import URL, HEADERS


api_key = "2511827112282642"

class ApiClient:

    def get_by_id(self, params, path="/api.php/{api_key}/{id_hero}"):
        path = path.format(**params)
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
        )
        response.raise_for_status()
        return response

    def get_power_by_hero_id(self, params, path="/api.php/{api_key}/{id_hero}/powerstats"):
        path = path.format(**params)
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
        )
        response.raise_for_status()
        return response
