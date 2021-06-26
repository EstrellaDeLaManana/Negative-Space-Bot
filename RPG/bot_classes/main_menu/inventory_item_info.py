from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import INVENTORY_INFO
from RPG.game_classes.items.base_weapon import BaseWeapon
from RPG.game_classes.items.base_armor import BaseArmorSet


class InventoryItemInfo(BaseHandler):
    def __init__(self, game):
        super().__init__(game, INVENTORY_INFO)
        self.item = None

    def show(self, call):
        self.item = self.game.player.inventory[int(call.data)]
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)
        if isinstance(self.item, BaseWeapon) or isinstance(self.item, BaseArmorSet):
            self.reply_keyboard.row('✔Equipar', '✖Tirar')
            self.reply_keyboard.row('🔄Recargar', '⬅Atrás')
        else:
            self.reply_keyboard.row('✔Utilizar', '✖Tirar')
            self.reply_keyboard.row('⬅Atrás')
        self.game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        self.game.bot.delete_message(call.message.chat.id, call.message.message_id)
        self.game.bot.send_message(call.message.chat.id,
                                   self.item.get_info(),
                                   parse_mode='Markdown',
                                   reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '✔Equipar':
            if isinstance(self.item, BaseWeapon) or isinstance(self.item, BaseArmorSet):
                self.item.use(self.game.player)
            else:
                self.show_input_error(message)
            self.game.inventory.start(message)
        elif message.text == '✔Utilizar':
            if isinstance(self.item, BaseWeapon) or isinstance(self.item, BaseArmorSet):
                self.show_input_error(message)
            else:
                self.item.use(self.game.player)
            self.game.inventory.start(message)
        elif message.text == '🔄Recargar':
            if isinstance(self.item, BaseWeapon):
                self.game.bot.send_message(message.chat.id, self.item.reload(self.game.player))
            else:
                self.show_input_error(message)
            self.game.inventory.start(message)
        elif message.text == '✖Tirar':
            self.game.player.drop_item(self.item)
            self.game.inventory.start(message)
        elif message.text == '⬅Atrás':
            self.game.inventory.start(message)
        else:
            self.show_input_error(message)
