from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from RPG.bot_classes.base_handler import BaseHandler


class TradeMenu(BaseHandler):  # Clase base para todos los comerciantes
    def __init__(self, game, npc, game_state, buy_state, sell_state, description, stock_products, factor):
        super().__init__(game, game_state)
        self.npc = npc
        self.buy_state = buy_state
        self.sell_state = sell_state
        self.description = description
        self.stock_products = stock_products
        self.max_stock_products = 5
        self.factor = factor

    def show(self, message):
        reply_keyboard = ReplyKeyboardMarkup(True, True)
        reply_keyboard.row('⬇️Comprar', '⬆️Vender')
        reply_keyboard.row('⬅Atrás')
        self.npc.say(message, self.description, reply_markup=reply_keyboard)

    def handle(self, message):
        if message.text == '⬇️Comprar':
            self.show_buy(message)
        elif message.text == '⬆️Vender':
            self.show_sell(message)
        elif message.text == '⬅Atrás':
            self.npc.start(message)
        else:
            self.npc.show_input_error(message)

    def show_buy(self, message):  # Muestra el surtido
        self.game.state = self.buy_state
        trader_inline_keyboard = InlineKeyboardMarkup()
        for product in self.stock_products:
            btn = InlineKeyboardButton(text=f'{product} 💵{int(product.price * self.factor)}',
                                       callback_data=str(self.stock_products.index(product)))
            trader_inline_keyboard.add(btn)
        close_btn = InlineKeyboardButton(text='⬅Atrás',
                                         callback_data='back')
        trader_inline_keyboard.add(close_btn)
        self.game.bot.send_message(message.chat.id, '🎒Mercancía:', reply_markup=trader_inline_keyboard)

    def handle_buy(self, call):  # Maneja la selección del artículo de la gama
        if call.data == 'back':
            self.game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            self.game.bot.delete_message(call.message.chat.id, call.message.message_id)
            self.start(call.message)
        else:
            item = self.stock_products[int(call.data)]
            bought_message = self.game.player.buy_item(item, self.factor)
            if bought_message[0]:
                self.stock_products.remove(item)
                self.game.bot.send_message(call.message.chat.id, f'{bought_message[1]} {item.name}')
            else:
                self.game.bot.send_message(call.message.chat.id,
                                           f'No se pudo comprar {item.name}: {bought_message[1]}')
            self.game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            self.game.bot.delete_message(call.message.chat.id, call.message.message_id)
            self.show_buy(call.message)

    def show_sell(self, message):  # Muestra el inventario para la venta
        self.game.state = self.sell_state
        trader_inline_keyboard = InlineKeyboardMarkup()
        for item in self.game.player.inventory:
            if item is not None:
                btn = InlineKeyboardButton(text=f'{item} 💵{int(item.price / self.factor)}',
                                           callback_data=f'{self.game.player.inventory.index(item)}')
                trader_inline_keyboard.add(btn)
        close_btn = InlineKeyboardButton(text='⬅Atrás',
                                         callback_data='back')
        trader_inline_keyboard.add(close_btn)
        self.game.bot.send_message(message.chat.id, '🎒Inventario:', reply_markup=trader_inline_keyboard)

    def handle_sell(self, call):  # Procesa el artículo seleccionado del inventario
        if call.data == 'back':
            self.game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            self.game.bot.delete_message(call.message.chat.id, call.message.message_id)
            self.start(call.message)
        else:
            item = self.game.player.inventory[int(call.data)]
            self.game.player.sell_item(item, self.factor)
            self.game.bot.send_message(call.message.chat.id, f'Vendido con éxito: {item}')
            self.game.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            self.game.bot.delete_message(call.message.chat.id, call.message.message_id)
            self.show_sell(call.message)
