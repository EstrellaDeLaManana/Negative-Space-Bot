from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import EQUIPMENT_ARMOR_INFO


class EquipmentArmorInfo(BaseHandler):
    def __init__(self, game):
        super().__init__(game, EQUIPMENT_ARMOR_INFO)
        self.reply_keyboard.row('⬇️ Retirar', '✖️ Tirar')
        self.reply_keyboard.row('⬅️ Atrás')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, f'{self.game.player.armor_set.get_info()}',
                                   parse_mode='Markdown', reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '⬇️ Retirar':
            if self.game.player.add_item(self.game.player.armor_set):
                self.game.bot.send_message(message.chat.id, f'{self.game.player.armor_set.name} ¡filmado con éxito!')
                self.game.player.armor -= self.game.player.armor_set.armor
                self.game.player.armor_set = None
            else:
                self.game.bot.send_message(message.chat.id,
                                           f'No se pudo quitar {self.game.player.armor_set.name}: ¡el inventario está lleno!')
            self.game.equipment.start(message)
        elif message.text == '✖️ Tirar':
            self.game.bot.send_message(message.chat.id, f'{self.game.player.armor_set.name} ¡lanzado con éxito!')
            self.game.player.armor -= self.game.player.armor_set.armor
            self.game.player.armor_set = None
            self.game.equipment.start(message)
        elif message.text == '⬅️ Atrás':
            self.game.equipment.start(message)
        else:
            self.show_input_error(message)
