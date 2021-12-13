from random import randint
import pytest

from superheroes.clients.api_client import ApiClient
from superheroes.helpers.base_helpers import who_stronger


@pytest.fixture
def get_two_random_heroes():
    """
    create a random number in range [1-720] = hero's id
    check that given random hero has a field 'power'
    return: dict = {hero: power}
    """
    rivals, n = list(), 0
    while n != 2:
        data = {'id_hero': randint(1, 720)}
        hero = ApiClient().get_power_by_hero_id(params=data).json()
        if hero.get("power") != 'null':
            rivals.append({
                "id": hero.get("id"),
                "name": hero.get("name"),
                "power": int(hero.get("power"))})
            n += 1
    print(f'\nHero1: {rivals[0]}\nHero2: {rivals[1]}')
    hero1, hero2 = rivals
    winner_name = who_stronger(hero1, hero2)
    return hero1.get("id"), hero2.get("id"), winner_name
