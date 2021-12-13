from random import randint
import pytest
from superheroes.clients.api_client import ApiClient


@pytest.mark.parametrize('rand_hero_id', [randint(1, 700) for _ in range(5)])
def test_superhero_example(rand_hero_id):
    """ Test get 5 randomly chosen superheroes """
    data = {
        "id_hero": rand_hero_id
    }
    hero = ApiClient().get_by_id(params=data).json()
    print(hero)
    return hero
