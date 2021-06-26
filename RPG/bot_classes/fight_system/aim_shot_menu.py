from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import FIGHT_SYSTEM_AIM_SHOT_MENU


class AimShotMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, FIGHT_SYSTEM_AIM_SHOT_MENU)
        self.reply_keyboard.row('😡 Cabeza-5 OD')
        self.reply_keyboard.row('🧥 Cuerpo - 3 OD')
        self.reply_keyboard.row('🦵 🏻 Extremidades - 4 OD')
        self.reply_keyboard.row('⬅️ Atrás')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, 'Elige a qué parte del cuerpo va a apuntar.')
        self.game.bot.send_message(message.chat.id,
                                   f'Puntos de acción disponibles: *{self.game.fight_system.action_points}*',
                                   parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '😡 Cabeza-5 OD':
            if self.game.fight_system.action_points >= 5:
                if self.game.player.laser_ammo >= 1:
                    self.game.fight_system.player_attack(message, 1, 5, 3, 9, self.reply_keyboard)
                else:
                    self.game.fight_system.show_ammo_error(message)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '🧥 Cuerpo - 3 OD':
            if self.game.fight_system.action_points >= 3:
                if self.game.player.laser_ammo >= 1:
                    self.game.fight_system.player_attack(message, 1, 3, 7, 3, self.reply_keyboard)
                else:
                    self.game.fight_system.show_ammo_error(message)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '🦵 🏻 Extremidades - 4 OD':
            if self.game.fight_system.action_points >= 4:
                if self.game.player.laser_ammo >= 1:
                    self.game.fight_system.player_attack(message, 1, 4, 5, 5, self.reply_keyboard)
                else:
                    self.game.fight_system.show_ammo_error(message)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '⬅️ Atrás':
            self.game.fight_system.weapon_use_menu.start(message)
        else:
            self.show_input_error(message)
