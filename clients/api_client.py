import requests
from superheroes.settings import URL, HEADERS


class ApiClient:

    def get_by_id(self, params, path="/api.php/2511827112282642/{id_hero}"):
        path = path.format(**params)
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
        )
        response.raise_for_status()
        return response

    def get_power_by_hero_id(self, params, path="/api.php/2511827112282642/{id_hero}/powerstats"):
        path = path.format(**params)
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
        )
        response.raise_for_status()
        return response
