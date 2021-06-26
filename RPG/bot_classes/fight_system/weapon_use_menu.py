from telebot.types import ReplyKeyboardMarkup

from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import FIGHT_SYSTEM_WEAPON_USE


class FightSystemWeaponUseMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, FIGHT_SYSTEM_WEAPON_USE)

    def show(self, message):  # Выводит меню использования оружия
        self.game.state = FIGHT_SYSTEM_WEAPON_USE
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)
        self.reply_keyboard.row('💥 Solo tiro - 1 OD', '💥 💥 💥 Disparo ráfaga - 3 OD')
        self.reply_keyboard.row('🎯 Tiro de puntería - 4 OD', '🔄 Recarga - 2 OD')
        self.reply_keyboard.row('⬅️ Atrás')
        self.game.fight_system.show_action_points(message, self.reply_keyboard)

    def handle(self, message):
        if message.text == '💥 Solo tiro - 1 OD':
            if self.game.fight_system.action_points >= 1:
                if self.game.player.weapon.loaded_ammo >= 1:
                    self.game.fight_system.player_attack(message, 1, 1, 7, 1, self.reply_keyboard)
                else:
                    self.game.fight_system.show_ammo_error(message)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '💥 💥 💥 Disparo ráfaga - 3 OD':
            if self.game.fight_system.action_points >= 3:
                if self.game.player.weapon.loaded_ammo >= 3:
                    self.game.fight_system.player_attack(message, 3, 3, 5, 3, self.reply_keyboard)
                else:
                    self.game.fight_system.show_ammo_error(message)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '🎯 Tiro de puntería - 4 OD':
            self.game.fight_system.aim_shot_menu.start(message)
        elif message.text == '🔄 Recarga - 2 OD':
            if self.game.fight_system.action_points >= 2:
                self.game.bot.send_message(message.chat.id, self.game.player.weapon.reload(self.game.player),
                                           reply_markup=self.reply_keyboard)
                self.game.fight_system.action_points -= 2
                self.game.fight_system.show_action_points(message, self.reply_keyboard)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '⬅️ Atrás':
            self.game.fight_system.player_turn.start(message)
        else:
            self.show_input_error(message)
