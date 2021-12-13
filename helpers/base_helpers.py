from re import findall, IGNORECASE
from superheroes.clients.http_client import HttpClient


def find_all_women():
    """
    Find all female heroes. return dict
    """
    page = HttpClient().get_heroes_list_page().text
    heroes_list = findall('<td>(.*?)</td>', page, IGNORECASE)
    length, only_women = len(heroes_list), dict()
    for i in range(0, length, 2):
        if 'woman' in heroes_list[i+1].lower():
            woman = {heroes_list[i]: heroes_list[i+1]}
            only_women.update(woman)
    return only_women


def who_stronger(hero1, hero2):
    """
    compare two superheroes by their power
    : return name of hero that turn to be stronger
    """
    name1, name2 = hero1.get("name"), hero2.get("name")
    power1, power2 = hero1.get("power"), hero2.get("power")
    if power1 == power2:
        return "Parity"
    return name1 if power1 > power2 else name2
