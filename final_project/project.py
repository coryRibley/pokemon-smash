import time
import random
import sys
from custom_library import Pokemon, Move, strike, Style, print_with_color

# NORMAL MOVES
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
yawn = Move(
    "Yawn",
    "normal",
    0,
    0,
    effect="sleep",
    cooldown=3,
    desc="puts the enemy to sleep in two turns",
)
body_slam = Move(
    "Body Slam",
    "normal",
    1.25,
    15,
    effect="chncestun",
    cooldown=2,
    desc="does little dmg, but has a chance to stun",
)
swap = Move(
    "Swap", "normal", 0, 0, effect="swap", desc="swap with another pokemon on the bench"
)
# FIRE MOVES
fire_spin = Move(
    "Fire Spin", "fire", 1.5, 15, effect=None, desc="fire move doing moderate dmg"
)
inferno = Move(
    "Inferno",
    "fire",
    2.2,
    30,
    effect="burn",
    cooldown=2,
    desc="game-changing move, deals large dmg, sets enemy aflame",
)
# WATER MOVES
water_gun = Move(
    "Water Gun",
    "water",
    1.25,
    15,
    effect=None,
    desc="basic water move, doing little dmg",
)
hydro_pump = Move(
    "Hydro Pump",
    "water",
    3,
    30,
    effect=None,
    cooldown=2,
    desc="earth-shattering water move",
)
# GRASS MOVES
vine_whip = Move(
    "Vine Whip",
    "grass",
    1.25,
    5,
    effect=None,
    desc="basic grass move dealing little dmg",
)
grass_knot = Move(
    "Grass Knot",
    "grass",
    1.5,
    15,
    effect=None,
    desc="grass move that deals moderate dmg",
)
solar_beam = Move(
    "Solar Beam",
    "grass",
    3,
    15,
    effect="dmgdelay",
    cooldown=2,
    desc="tremendous grass blast, deals dmg next turn only",
)
# ICE MOVES
ice_wind = Move(
    "Icy Wind",
    "ice",
    0.5,
    0,
    effect="freeze",
    cooldown=3,
    desc="deals very little ice dmg, but freezes the enemy",
)
ice_shard = Move(
    "Ice Shard", "ice", 1.75, 15, effect=None, desc="frosty move, dealing moderate dmg"
)
ice_beam = Move(
    "Ice Beam",
    "ice",
    1.25,
    15,
    effect="chncefreeze",
    desc="deals little ice dmg with a chance to freeze",
)
# ELECTRIC MOVES
spark = Move("Spark", "electric", 1.2, 5, effect=None, desc="basic electric move")
discharge = Move(
    "Discharge",
    "electric",
    1.75,
    15,
    cooldown=2,
    desc="moderately powerful electric attack",
)
thunder = Move(
    "Thunder", "electric", 2.5, 30, cooldown=3, desc="insanely-powerful electric storm"
)
# Instantiate all pokemon below
charmander = Pokemon(
    "Charmander", 92, 15, "fire", "one", scratch, fire_spin, inferno, swap
)
squirtle = Pokemon(
    "Squirtle", 95, 11, "water", "one", tackle, water_gun, ice_wind, hydro_pump, swap
)
bulbasaur = Pokemon(
    "Bulbasaur", 83, 15, "grass", "one", take_down, vine_whip, solar_beam, swap
)
lapras = Pokemon(
    "Lapras", 101, 12, "ice", "two", ice_shard, ice_beam, hydro_pump, body_slam, swap
)
pikachu = Pokemon(
    "Pikachu", 79, 17, "electric", "two", spark, discharge, thunder, grass_knot, swap
)
snorlax = Pokemon("Snorlax", 114, 12, "normal", "two", tackle, body_slam, yawn, swap)
pokemon_list = [charmander, squirtle, bulbasaur, snorlax, lapras, pikachu]

def get_start_desc(player_one, player_two):
    first_desc = f"{player_one}'s team:\n{charmander}\n{squirtle}\n{bulbasaur}\n\n"
    second_desc = f"{player_two}'s team:\n{snorlax}\n{lapras}\n{pikachu}\n\n"
    return first_desc + second_desc

def main():

    try:
        start()
        print("\nLet's Fight!")
        time.sleep(0.5)
        print(get_start_desc(charmander.team, snorlax.team))
        time.sleep(5.0)
        if random.randint(1, 100) > 50:
            first = charmander.team
            fpm = charmander
            spm = snorlax
        else:
            first = snorlax.team
            fpm = snorlax
            spm = charmander
        print(f"Fate has decided that {first} is going first!")
        time.sleep(2.5)
        fight(fpm, spm)
    except KeyboardInterrupt:
        sys.exit("\nGotta catch em all!")


def start():
    trainer_one = input("What is trainer one's name? ").capitalize()
    trainer_two = input("What is trainer two's name? ").capitalize()
    for poke in [charmander, squirtle, bulbasaur, lapras, pikachu, snorlax]:
        if poke.team == "one":
            poke.team = trainer_one
        if poke.team == "two":
            poke.team = trainer_two


def fight(poke1, poke2):

    initialize_fight(poke1, poke2)
    mv = select_move(poke1, poke2)

    if random.randint(1, 100) >= mv.miss:
        handle_hit(poke1, poke2, mv)
    else:
        print(f"{mv} missed!")
    while poke1.alive and poke2.alive:
        time.sleep(3.0)
        fight(poke2, poke1)


def initialize_fight(poke1, poke2):
    if poke1.on_fire:
        poke1.burn()
        time.sleep(1.5)
        print(f"{poke1} has sustained burn damage...")
        time.sleep(1.0)
    lower_cooldown(poke1)
    time.sleep(0.5)
    print(f"\nIt's {poke1.team}'s turn!")
    time.sleep(1.5)
    temp_hp = poke1.hp

    poke1.delayed_eff(poke2)
    if poke1.delay_tmr == 0:
        if poke1.asleep:
            time.sleep(1.5)
            print(f"\n{poke1} has fallen asleep...")
            time.sleep(3.0)
            poke1.saved_move = None
            poke1.asleep = False
            fight(poke2, poke1)
        if temp_hp != poke1.hp:
            time.sleep(1.5)
            print(f"{poke1.saved_move} hit {poke1}!")
            time.sleep(1.5)
            if poke1.hp > 0:
                print(f"{poke1} has {round(poke1.hp)} hp\n")
            else:
                print(
                    f"\n{'-' * (len(poke2.name) + 13)}\n{poke2} has fainted!\n{'-' * (len(poke2.name) + 13)}\n"
                )
                time.sleep(1.5)
                if len(get_swap_list(poke2)) > 0:
                    swap_pokemon(poke2, poke1)
                else:
                    sys.exit(f"🎉🥳{poke1.team} has come out on top!!!🥳🎉".upper())
            poke1.saved_move = None



def select_move(poke1, poke2):

    print(f"{poke1} has {len(poke1.moves)} moves:\n")
    time.sleep(0.5)
    for i, move in enumerate(poke1.moves):
        move.set_eff(poke2)
        if move.cd_timer > 0 or (
            move.effect == "swap" and len(get_swap_list(poke1)) == 0
        ):
            print_with_color(f"{i + 1} {strike(str(move))}", brightness=Style.DIM)
            time.sleep(0.5)
        else:
            print(i + 1, move.get_eff_color())
            print_with_color(f"{move.desc}", brightness=Style.DIM)
            time.sleep(0.5)
    try:
        mv = poke1.moves[int(input("\nEnter a number to select a move. ")) - 1]
        if mv.cd_timer > 0:
            raise ValueError
        time.sleep(0.5)
    except (IndexError, ValueError):
        print("That is not a valid move!")
        while True:
            try:
                mv = poke1.moves[int(input()) - 1]
                if mv.cd_timer > 0 or (
                    move.effect == "swap" and len(get_swap_list(poke1)) == 0
                ):
                    raise ValueError
                time.sleep(0.5)
                break
            except (IndexError, ValueError):
                ...
    if mv.effect == "swap":
        swap_pokemon(poke1, poke2)
    time.sleep(1.0)
    print(f"\n{poke2} has {round(poke2.hp)} hp")
    time.sleep(0.5)
    print(f"\n{poke1} used {mv}\n")
    time.sleep(2.5)
    return mv


def handle_hit(poke1, poke2, mv):
    match mv.effect:
        case "sleep":
            print(f"{poke2} is getting sleepy...")
            time.sleep(2.5)
            poke2.delay_tmr = 1
            poke2.saved_move = mv
            if mv.cooldown:
                mv.cd_timer = mv.cooldown
            fight(poke2, poke1)
        case "dmgdelay":
            print("All wind stands still...")
            time.sleep(2.5)
            poke2.delay_tmr = 1
            poke2.saved_move = mv
            if mv.cooldown:
                mv.cd_timer = mv.cooldown
            fight(poke2, poke1)
    print(f"{mv} hit {poke2}")
    poke1.attack(poke2, mv)
    time.sleep(1.5)
    if mv.eff == True:
        print(f"{mv} was super effective!")
        time.sleep(1.5)
    elif mv.eff == False:
        print(f"{mv} was not very effective...")
        time.sleep(1.5)
    if poke2.alive:
        print(f"{poke2} has {round(poke2.hp)} hp left!")
        if mv.effect == "dmgself":
            time.sleep(0.5)
            print(f"{poke1} sustained damage, as well.")
            time.sleep(1.5)
            poke1.dmgself(mv)
            print(f"{poke1} has {round(poke1.hp)} hp left!")
    else:
        print(
            f"\n{'-' * (len(poke2.name) + 13)}\n{poke2} has fainted!\n{'-' * (len(poke2.name) + 13)}\n"
        )
        time.sleep(1.5)
        if len(get_swap_list(poke2)) > 0:
            swap_pokemon(poke2, poke1)
        else:
            sys.exit(f"🎉🥳{poke1.team} has come out on top!!!🥳🎉".upper())
    if mv.cooldown:
        mv.cd_timer = mv.cooldown
    if mv.effect == "freeze" or (mv.effect == "chncefreeze" and get_30()):
        time.sleep(1.5)
        print(f"{poke2} has been frozen!")
        poke2.frozen = True
        time.sleep(3.0)
        fight(poke1, poke2)
    elif mv.effect == "chncefreeze":
        time.sleep(1.5)
        print(f"{mv} did not freeze {poke2}.")
    elif mv.effect == "burn":
        time.sleep(1.5)
        print(f"{poke2} is on fire!")
        poke2.on_fire = True

    if mv.effect == "chncestun" and get_30() and poke2.saved_move == None:
        time.sleep(1.5)
        print(f"{poke2} has been stunned!")
        poke2.frozen = True
        time.sleep(3.0)
        fight(poke1, poke2)
    elif mv.effect == "chncestun":
        time.sleep(1.5)
        print(f"{mv} did not stun {poke2}.")
        poke2.frozen = False


def get_30():
    return random.randint(1, 100) > 30


def swap_pokemon(poke1, poke2):
    swap_len = len(get_swap_list(poke1))

    print(f"{poke1.team} has {swap_len} pokemon left.")
    time.sleep(0.5)
    for i, poke in enumerate(get_swap_list(poke1)):
        print(i + 1, poke)
        time.sleep(0.5)
    try:
        poke = get_swap_list(poke1)[
            int(input("\nEnter a number to select a pokemon to swap with. ")) - 1
        ]
    except (IndexError, ValueError):
        print("That is not a valid pokemon!")
        while True:
            try:
                poke = get_swap_list(poke1)[int(input()) - 1]
                if not poke.alive:
                    raise ValueError
                time.sleep(0.5)
                break
            except (IndexError, ValueError):
                ...
    print(f"{poke1.team} has replaced {poke1} with {poke}")
    fight(poke2, poke)


def lower_cooldown(poke1):
    for move in poke1.moves:
        if move.cd_timer > 0:
            move.cd_timer -= 1


def get_swap_list(poke1):
    swap_list = []
    for poke in pokemon_list:
        if poke.team == poke1.team and poke != poke1 and poke.alive:
            swap_list.append(poke)
    return swap_list


if __name__ == "__main__":
    main()
