import pygame
from pygame.locals import *
from Constants import *
from Models.Battle import *
from Models.Pokemon import *

pokemon1 = Pokemon("Bulbasaur", 100, 11, 3)
pokemon2 = Pokemon("Blaziken", 100, 9, 1)
pokemon1.current_hp = 45
pokemon2.current_hp = 45

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
    HP: 45,
    ATK: 49,
    DEF: 49,
    SPATK: 65,
    SPDEF: 65,
    SPEED: 45
}
pokemon2.ev = {
    HP: 0,
    ATK: 0,
    DEF: 0,
    SPATK: 0,
    SPDEF: 0,
    SPEED: 0
}
pokemon2.iv = {
    HP: 21,
    ATK: 21,
    DEF: 21,
    SPATK: 21,
    SPDEF: 21,
    SPEED: 21
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


def load_resources():
    load_pokemon_image(pokemon1, True)
    load_pokemon_image(pokemon2, False)


def render(screen):
    screen.fill((255,255,255))
    render_pokemon(screen, pokemon1, pokemon2)
    pygame.display.update()


def update():
    pass


def load_pokemon_image(pokemon, is_player):
    pokemon_name = pokemon.name.lower()
    if is_player:
        pokemon_img = pygame.image.load('Resources/Pokemon/'+pokemon_name+"_back.png")
        pokemon_img = pygame.transform.scale(pokemon_img, (400, 400))
        pokemon.renderer = pokemon_img
    else:
        pokemon_img = pygame.image.load('Resources/Pokemon/'+pokemon_name+".png")
        pokemon_img = pygame.transform.scale(pokemon_img, (400, 400))
        pokemon.renderer = pokemon_img


def render_pokemon(screen, pokemon1, pokemon2):
    pokemon1.render(screen, (10, 200))
    pokemon2.render(screen, (440, -50))


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption("Mc Pokémon")
    load_resources()
    clock = pygame.time.Clock()
    stopped = False
    clock.tick(60)
    while not stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sttoped = True
        update()
        render(screen)


if __name__ == "__main__":
    main()

# while not battle.is_finished():
#    command1 = ask_command(pokemon1)
#    command2 = ask_command(pokemon2)

#    turn = Turn()
#    turn.command1 = command1
#    turn.command2 = command2

#    if turn.can_start():
#        battle.execute_turn(turn)
#        battle.print_current_status()
