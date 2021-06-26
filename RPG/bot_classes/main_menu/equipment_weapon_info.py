from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import EQUIPMENT_WEAPON_INFO


class EquipmentWeaponInfo(BaseHandler):
    def __init__(self, game):
        super().__init__(game, EQUIPMENT_WEAPON_INFO)
        self.reply_keyboard.row('⬇️ Retirar', '✖️ Tirar')
        self.reply_keyboard.row('🔄 Recargar', '⬅️ Atrás')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, f'{self.game.player.weapon.get_info()}',
                                   parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '⬇️ Retirar':
            if self.game.player.add_item(self.game.player.weapon):
                self.game.bot.send_message(message.chat.id, f'{self.game.player.weapon.name} ¡filmado con éxito!')
                self.game.player.weapon = None
            else:
                self.game.bot.send_message(message.chat.id,
                                           f'No se pudo quitar {self.game.player.weapon.name}: ¡el inventario está lleno!')
            self.game.equipment.start(message)
        elif message.text == '✖️ Tirar':
            self.game.bot.send_message(message.chat.id, f'{self.game.player.weapon.name} ¡lanzado con éxito!')
            self.game.player.weapon = None
            self.game.equipment.start(message)
        elif message.text == '🔄 Recargar':
            self.game.bot.send_message(message.chat.id, self.game.player.weapon.reload(self.game.player))
            self.game.equipment.start(message)
        elif message.text == '⬅️ Atrás':
            self.game.equipment.start(message)
        else:
            self.show_input_error(message)
