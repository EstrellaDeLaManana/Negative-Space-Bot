import telebot
from RPG.bot_classes.base_handler import BaseHandler
from RPG.game_states import INVENTORY


class Inventory(BaseHandler):
    def __init__(self, game):
        super().__init__(game, INVENTORY)

    def start(self, message):
        self.game.players[message.chat.id].state = self.game_state
        self.show(message)

    def show(self, message):
        inventory_inline_keyboard = telebot.types.InlineKeyboardMarkup()
        for item in self.game.players[message.chat.id].inventory:
            if item is None:
                btn = telebot.types.InlineKeyboardButton(text='<Пустой слот>',
                                                         callback_data=str(
                                                             self.game.players[
                                                                 message.chat.id].inventory.index(item)))
            else:
                btn = telebot.types.InlineKeyboardButton(text=str(item),
                                                         callback_data=str(
                                                             self.game.players[
                                                                 message.chat.id].inventory.index(item)))
            inventory_inline_keyboard.add(btn)
        close_btn = telebot.types.InlineKeyboardButton(text='⬅Назад',
                                                       callback_data='back')
        inventory_inline_keyboard.add(close_btn)
        self.game.bot.send_message(message.chat.id, '🎒Инвентарь:', reply_markup=inventory_inline_keyboard)

    def handle(self, call):
        if call.data == 'back':
            self.game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            self.game.bot.delete_message(call.message.chat.id, call.message.message_id)
            self.game.main_menu.start(call.message)
        else:
            self.game.inventory_item_info.start(call)
