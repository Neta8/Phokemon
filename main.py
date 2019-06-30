from Constants import *
from Models.Battle import *
from Models.Pokemon import *

pokemon1 = Pokemon("Bulbasaur", 100, 11, 3)
pokemon2 = Pokemon("Garchomp", 78, 15, 4)
pokemon1.current_hp = 45
pokemon2.current_hp = 289

pokemon1.baseStats = {
    HP: 45,
    ATK: 49,
    DEF: 49,
    SPATK: 65,
    SPDEF: 65,
    SPEED: 45
}
pokemon1.ev = {
    HP: 0,
    ATK: 0,
    DEF: 0,
    SPATK: 0,
    SPDEF: 0,
    SPEED: 0
}
pokemon1.iv = {
    HP: 21,
    ATK: 21,
    DEF: 21,
    SPATK: 21,
    SPDEF: 21,
    SPEED: 21
}
pokemon1.compute_stats()
print(pokemon1.stats)
pokemon2.baseStats = {
    HP: 108,
    ATK: 130,
    DEF: 95,
    SPATK: 80,
    SPDEF: 85,
    SPEED: 102
}
pokemon2.ev = {
    HP: 74,
    ATK: 190,
    DEF: 91,
    SPATK: 48,
    SPDEF: 84,
    SPEED: 23
}
pokemon2.iv = {
    HP: 24,
    ATK: 12,
    DEF: 30,
    SPATK: 16,
    SPDEF: 23,
    SPEED: 5
}
pokemon2.compute_stats()
print(pokemon2.stats)

pokemon1.attacks = [Attack("TAIL WHIP", 11, PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [Attack("SCRATCH", 0, PHYSICAL, 10, 10, 100)]

battle = Battle(pokemon1, pokemon2)


def ask_command(pokemon):
    command = None
    while not command:
        tmp_command = input("What should "+pokemon.name+" do?").split(" ")
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command


while not battle.is_finished():
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        battle.execute_turn(turn)
        battle.print_current_status()
