import pygame
from functools import partial
from pygame.locals import *
from Constants import *
from Models.Battle import *
from Models.Pokemon import *
from Models.Button import Button


class Game:

    def __init__(self):
        self.buttons = []
        pygame.init()

        self.screen = pygame.display.set_mode((160*4, 144*4))
        pygame.display.set_caption("Mc Pokémon")

        clock = pygame.time.Clock()
        clock.tick(60)

        self.pokemon1 = Pokemon("Bulbasaur", 100, 11, 3)
        self.pokemon2 = Pokemon("Bulbasaur", 100, 11, 3)
        self.init_pokemon_stats()

        self.pokemon1.attacks = [
            Attack("TAIL WHIP", 11, PHYSICAL, 10, 10, 100),
            Attack("TACKLE", 1, PHYSICAL, 10, 10, 100)
        ]
        self.pokemon2.attacks = [Attack("SCRATCH", 0, PHYSICAL, 10, 10, 100)]

        for idx, attack in enumerate(self.pokemon1.attacks):
            function_turn = partial(self.make_turn, index=idx)
            self.buttons.append(
                Button(idx*100, 0, 100, 40, attack.name, function_turn)
            )
        self.load_resources()
        print('resources loaded succesfully')
        self.battle = Battle(self.pokemon1, self.pokemon2)

        self.stopped = False
        print('Initialization finished')

    def process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.stopped = True
            for button in self.buttons:
                button.handle_event(event, self)

    def load_resources(self):
        self.load_pokemon_image(self.pokemon1, True)
        self.load_pokemon_image(self.pokemon2, False)

    def load_pokemon_image(self, pokemon, is_player):
        pokemon_name = pokemon.name.lower()
        if is_player:
            pokemon_img = pygame.image.load('Resources/Pokemon/' + pokemon_name + "_back.png")
            pokemon_img = pygame.transform.scale(pokemon_img, (200, 200))
            pokemon.renderer = pokemon_img
        else:
            pokemon_img = pygame.image.load('Resources/Pokemon/' + pokemon_name + ".png")
            pokemon_img = pygame.transform.scale(pokemon_img, (200, 200))
            pokemon.renderer = pokemon_img

    def init_pokemon_stats(self):
        self.pokemon1.current_hp = 45
        self.pokemon2.current_hp = 45

        self.pokemon1.baseStats = {
            HP: 45,
            ATK: 49,
            DEF: 49,
            SPATK: 65,
            SPDEF: 65,
            SPEED: 45
        }
        self.pokemon1.ev = {
            HP: 0,
            ATK: 0,
            DEF: 0,
            SPATK: 0,
            SPDEF: 0,
            SPEED: 0
        }
        self.pokemon1.iv = {
            HP: 21,
            ATK: 21,
            DEF: 21,
            SPATK: 21,
            SPDEF: 21,
            SPEED: 21
        }
        self.pokemon1.compute_stats()
        self.pokemon2.baseStats = {
            HP: 45,
            ATK: 49,
            DEF: 49,
            SPATK: 65,
            SPDEF: 65,
            SPEED: 45
        }
        self.pokemon2.ev = {
            HP: 0,
            ATK: 0,
            DEF: 0,
            SPATK: 0,
            SPDEF: 0,
            SPEED: 0
        }
        self.pokemon2.iv = {
            HP: 21,
            ATK: 21,
            DEF: 21,
            SPATK: 21,
            SPDEF: 21,
            SPEED: 21
        }
        self.pokemon2.compute_stats()
        print(self.pokemon1.stats)
        print(self.pokemon2.stats)

    def render_pokemon(self):
        self.pokemon1.render(self.screen, (10, 200))
        self.pokemon2.render(self.screen, (440, 0))

    def render_buttons(self):
        for button in self.buttons:
            button.render(self)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.render_pokemon()
        self.render_buttons()
        pygame.display.update()

#    def build_mk_turn_f(self, index):
#        return self.make_turn(index)

    def make_turn(self, index):
        print('Using attack', index)
        turn = Turn()
        turn.command1 = Command({DO_ATTACK: index})
        turn.command2 = Command({DO_ATTACK: 0})

        if turn.can_start():
            self.battle.execute_turn(turn)
            self.battle.print_current_status()
