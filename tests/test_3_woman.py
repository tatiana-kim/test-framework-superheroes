import pytest
from hamcrest import assert_that, equal_to

from superheroes.clients.api_client import ApiClient
from superheroes.helpers.base_helpers import find_all_women


@pytest.mark.parametrize('women', find_all_women())
def test_is_women(women):
    """ check that method return only female superhero """
    data = {
        'id_hero': women
    }
    hero_women = ApiClient().get_by_id(params=data).json()
    print(hero_women.get("name"))
    gender = hero_women.get('appearance').get('gender')
    assert_that(actual=gender,
                matcher=equal_to("Female"),
                reason=f'Gender of superhero is {gender} but should be "Female"')
