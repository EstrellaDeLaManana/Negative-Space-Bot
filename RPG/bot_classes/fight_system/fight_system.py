from random import randint
from time import sleep

from RPG.bot_classes.fight_system.aim_shot_menu import AimShotMenu
from RPG.bot_classes.fight_system.player_turn import FightSystemPlayerTurn
from RPG.bot_classes.fight_system.weapon_use_menu import FightSystemWeaponUseMenu
from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import FIGHT_SYSTEM


class FightSystem(BaseHandler):
    def __init__(self, game):
        super().__init__(game, FIGHT_SYSTEM)
        self.enemy = None
        self.player_turn_first = None
        self.max_action_points = 1
        self.action_points = 1
        self.player_turn = FightSystemPlayerTurn(game)
        self.weapon_use_menu = FightSystemWeaponUseMenu(game)
        self.aim_shot_menu = AimShotMenu(game)

    def check_player_first_turn(self):
        if self.game.player.perception > self.enemy.perception:
            player_turn_first = True
        elif self.game.player.perception < self.enemy.perception:
            player_turn_first = False
        else:
            if self.game.player.agility > self.enemy.agility:
                player_turn_first = True
            elif self.game.player.agility < self.enemy.agility:
                player_turn_first = False
            else:
                if self.game.player.luck > self.enemy.luck:
                    player_turn_first = True
                elif self.game.player.luck < self.enemy.luck:
                    player_turn_first = False
                else:
                    player_turn_first = bool(randint(0, 1))
        return player_turn_first

    def start_fight(self, message, enemy):  # Muestra un mensaje de Inicio de batalla y calcula quién recibirá el primer movimiento
        self.enemy = enemy
        self.game.player.in_fight = True
        self.game.bot.send_message(message.chat.id, self.enemy.fight_message)
        self.game.bot.send_message(message.chat.id, f'Ты Ты has entrado en combate con *{enemy.name}*⚔️', parse_mode='Markdown')
        if self.check_player_first_turn():
            self.player_turn.show(message)
        else:
            self.start_enemy_turn(message)

    def start_enemy_turn(self, message):  # Movimiento enemigo (IA primitiva, solo hace daño)
        self.game.bot.send_message(message.chat.id, f'{self.enemy.name} apunta...')
        sleep(2)
        self.game.bot.send_message(message.chat.id, self.enemy.attack(self.game.player, randint(4, 9), randint(1, 3)))
        self.player_turn.start(message)
        self.game.fight_system.check_enemy_dead(message)
        self.check_player_dead(message)

    def show_action_points(self, message, reply_keyboard):
        self.game.bot.send_message(message.chat.id,
                                   f'Puntos de acción disponibles: *{self.game.fight_system.action_points}*',
                                   parse_mode='Markdown', reply_markup=reply_keyboard)

    def show_action_points_error(self, message, reply_markup):  # Muestra error: falta OD
        self.game.bot.send_message(message.chat.id, '¡No hay suficientes puntos de acción!', reply_markup=reply_markup)

    def show_ammo_error(self, message):  # Muestra error: no hay suficiente munición
        self.game.bot.send_message(message.chat.id, '¡No hay suficiente munición!', reply_markup=self.reply_keyboard)

    def player_attack(self, message, ammo, ap, shot_accuracy, damage_coef, reply_keyboard):
        self.game.bot.send_message(message.chat.id,
                                   self.game.player.attack(self.game.fight_system.enemy, shot_accuracy, damage_coef))
        self.game.player.weapon.loaded_ammo -= ammo
        self.game.fight_system.action_points -= ap
        self.game.fight_system.show_action_points(message, reply_keyboard)
        self.game.fight_system.check_enemy_dead(message)
        self.game.fight_system.check_player_dead(message)

    def check_player_dead(self, message):
        if self.game.player.hp <= 0:
            self.game.bot.send_message(message.chat.id, 'Whoooops... supongo que estás muerto. Ve con tu inventario y '
                                                        'vuelve a la nave.')
            self.game.player.inventory = [None] * 5
            self.game.player.weapon = None
            self.game.player.armor_set = None
            self.game.player.in_fight = False
            self.game.spaceship.cabin.start(message)
        else:
            self.game.bot.send_message(message.chat.id, f'Te queda {self.game.player.hp} hp',
                                       reply_markup=self.reply_keyboard)

    def check_enemy_dead(self, message):
        if self.enemy.hp <= 0:
            self.game.bot.send_message(message.chat.id, f'{self.enemy.name} ¡muere en una terrible agonía! ¡Tú ganas!')
            self.game.player.in_fight = False
            self.game.current_location.enemy = None
            self.game.current_location.start(message)
        else:
            self.game.bot.send_message(message.chat.id, f'De {self.enemy.name} queda {self.enemy.hp} hp',
                                       reply_markup=self.reply_keyboard)
