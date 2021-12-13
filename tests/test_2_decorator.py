from random import randint
import pytest
from superheroes.clients.api_client import ApiClient
from superheroes.checkers.smoke_checker import smoke_check


@pytest.mark.parametrize("rand_id", [randint(1, 700) for _ in range(5)])
@smoke_check
def test_superhero_example(rand_id):
    """ Use decorator for randomly choose a hero's id """
    data = {
        "id_hero": rand_id
    }
    response = ApiClient().get_by_id(params=data).json()
    print(response)
    return response
