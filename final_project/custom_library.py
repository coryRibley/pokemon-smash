from colorama import init, Fore, Back, Style
from termcolor import colored

eff_dict = {
    "fire": [["fire", "water"], ["grass", "ice"]],
    "water": [["grass", "water"], ["fire"]],
    "grass": [["fire", "grass"], ["water"]],
    "electric": [["electric", "grass"], ["water"]],
    "ice": [["ice", "water", "fire"], ["grass"]],
}


class Pokemon:
    def __init__(self, name, hp, base_dmg, type, team, *moves):
        self.name = name
        self.hp = hp
        self.base_dmg = base_dmg
        self.type = type
        self.team = team
        self.moves = list(moves)
        self.alive = True
        self.frozen = False
        self.asleep = False
        self.delay_tmr = 0
        self.saved_move = None
        self.on_fire = False

    def __str__(self):
        if self.type == "water":
            text = colored(self.name, "blue", attrs=["bold"])
        if self.type == "fire":
            text = colored(self.name, "red", attrs=["bold"])
        if self.type == "grass":
            text = colored(self.name, "green", attrs=["bold"])
        if self.type == "normal":
            text = colored(self.name, "white", attrs=["bold"])
        if self.type == "electric":
            text = colored(self.name, "yellow", attrs=["bold"])
        if self.type == "ice":
            text = colored(self.name, "cyan", attrs=["bold"])
        return text

    def burn(self):
        self.hp -= 10

    def attack(self, other, mv):
        if mv.eff == True:
            eff_mult = 1.5
        elif mv.eff == False:
            eff_mult = 0.75
        else:
            eff_mult = 1
        other.hp -= int(self.base_dmg * mv.mult * eff_mult)

    def dmgself(self, mv):
        self.hp -= int((self.base_dmg * mv.mult) / 4)

    def delayed_eff(self, other):
        mv = self.saved_move
        if self.delay_tmr == 0:
            try:
                match mv.effect:
                    case "sleep":
                        self.asleep = True
                    case "dmgdelay":
                        if mv.eff == True:
                            eff_mult = 1.5
                        elif mv.eff == False:
                            eff_mult = 0.75
                        else:
                            eff_mult = 1
                        self.hp -= int(other.base_dmg * mv.mult * eff_mult)
            except AttributeError:
                ...
        else:
            self.delay_tmr -= 1

    def add_move(self, moves):
        for move in moves:
            self.moves.append(move)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp
        if self._hp <= 0:
            self.alive = False

    @property
    def base_dmg(self):
        return self._base_dmg

    @base_dmg.setter
    def base_dmg(self, base_dmg):
        self._base_dmg = base_dmg


class Move:
    def __init__(self, name, type, mult, miss, effect=None, cooldown=0, desc=""):
        self.name = name
        self.type = type
        self.mult = mult
        self.miss = miss
        self.effect = effect
        self.cooldown = cooldown
        self.desc = desc
        self.cd_timer = 0
        self.eff = None

    def set_eff(self, poke):
        for group in eff_dict:
            if group == self.type:
                if poke.type in eff_dict[group][0]:
                    self.eff = False
                elif poke.type in eff_dict[group][1]:
                    self.eff = True
                else:
                    self.eff = None

    def get_eff_color(self):
        if self.eff == True:
            return colored(self.name, "grey", "on_green")
        elif self.eff == False:
            return colored(self.name, "grey", "on_red")
        return self.name

    def __str__(self):
        return self.name


# essential for Windows environment
# init()
# all available foreground colors
FORES = [
    Fore.BLACK,
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE,
]
# all available background colors
BACKS = [
    Back.BLACK,
    Back.RED,
    Back.GREEN,
    Back.YELLOW,
    Back.BLUE,
    Back.MAGENTA,
    Back.CYAN,
    Back.WHITE,
]
# brightness values
BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]


def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)


def strike(text):
    result = ""
    for c in text:
        result = result + "\u0336" + c
    return result
