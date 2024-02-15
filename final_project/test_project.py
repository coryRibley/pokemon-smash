import pytest
from custom_library import Pokemon, Move
from project import select_move, get_swap_list, lower_cooldown

scratch = Move(
    "Scratch",
    "normal",
    1.0,
    5,
    effect=None,
    desc="basic normal move dealing little dmg",
)
tackle = Move(
    "Tackle", "normal", 1.0, 5, effect=None, desc="basic normal move dealing little dmg"
)
take_down = Move(
    "Take Down",
    "normal",
    2.5,
    15,
    effect="dmgself",
    desc="normal move dealing large dmg, but also dmgs user",
)
charmander = Pokemon(
    "Charmander", 1, 15, "fire", "one", scratch
)
squirtle = Pokemon(
    "Squirtle", 95, 11, "water", "one", tackle
)
bulbasaur = Pokemon(
    "Bulbasaur", 83, 15, "grass", "one", take_down
)

def test_select_move(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    result = select_move(charmander, squirtle)
    assert result == scratch

def test_get_swap_list():
    swap_list = get_swap_list(charmander)
    result = []
    for poke in swap_list:
        result.append(poke.name)
    assert result == ['Charmander', 'Squirtle', 'Bulbasaur']

def test_lower_cooldown():
    charmander.moves[0].cd_timer = 3
    lower_cooldown(charmander)
    assert charmander.moves[0].cd_timer == 2
