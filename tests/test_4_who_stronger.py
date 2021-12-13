import pytest
from hamcrest import assert_that, equal_to

from superheroes.clients.api_client import ApiClient
from superheroes.helpers.base_helpers import who_stronger


def test_who_stronger(get_two_random_heroes):
    """ compare the power of two superheroes """
    id1, id2, winner = get_two_random_heroes
    print("\nWinner from fixture:", winner)
    data1 = {'id_hero': id1}
    data2 = {'id_hero': id2}
    hero1 = ApiClient().get_power_by_hero_id(params=data1).json()
    hero2 = ApiClient().get_power_by_hero_id(params=data2).json()
    h1 = {"name": hero1.get('name'), "power": int(hero1.get('power'))}
    h2 = {"name": hero2.get('name'), "power": int(hero2.get('power'))}
    winner_check = who_stronger(h1, h2)
    print("\nWinner from test:", winner_check)
    assert_that(actual=winner_check,
                matcher=equal_to(winner),
                reason=f"Winner defined by fixture ({winner}) /"
                       f"doesn't match with winner from test ({winner_check})")
