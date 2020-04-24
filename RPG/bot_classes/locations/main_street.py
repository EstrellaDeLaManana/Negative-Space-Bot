from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.game_states import MAIN_STREET, MAIN_STREET_TRADER, MAIN_STREET_TRADER_BUY, MAIN_STREET_TRADER_SELL
from RPG.bot_classes.trader import Trader
from RPG.game_classes.base_weapon import BaseWeapon


class MainStreetLocation(BaseLocation):
    def __init__(self, bot_game):
        super().__init__(bot_game, MAIN_STREET, 'Небольшое поселение',
                         'Ты находишься на главной улице небольшого поселения, затярянного в песках этой планеты.'
                         'Перед собой ты видишь небольшую лавчонку, построенную из листов ржавого железа и'
                         'старой техники, а так же руины какого-то здания.')
        stock_products = [BaseWeapon('Лазерная винтовка', 15, 100, 'Лазерная батарея', 500),
                          BaseWeapon('Старое ружьё', 15, 100, 'Дробь', 150)]
        self.trader = Trader(self.bot_game, MAIN_STREET_TRADER, MAIN_STREET_TRADER_BUY, MAIN_STREET_TRADER_SELL,
                             'Ты подходишь к лавке, чтобы поторговаться', stock_products, stock_products, 1)

    def show(self, message):
        reply_keyboard = ReplyKeyboardMarkup(True, True)
        reply_keyboard.row('👳🏾‍♂️Торговец', '🏚Руины')
        reply_keyboard.row('📟Главное меню')
        self.bot_game.bot.send_message(message.chat.id, self.show_message, parse_mode='Markdown',
                                       reply_markup=reply_keyboard)
        for player_id in self.bot_game.players:
            if player_id != message.chat.id and self.bot_game.players[player_id].state == self.game_state:
                self.bot_game.bot.send_message(player_id, f'Ты видишь как на эту же главную улицу заходит игрок с'
                                                          f' именем {self.bot_game.players[message.chat.id].name}')
                self.bot_game.bot.send_message(message.chat.id, f'Ты видишь как на этой же улице уже находится игрок '
                                                                f'с именем {self.bot_game.players[player_id].name}')

    def handle(self, message):
        if message.text == '👳🏾‍♂️Торговец':
            self.trader.start(message)
        elif message.text == '🏚Руины':
            self.bot_game.ruined_house_location[message.chat.id].start(message)
        elif message.text == '📟Главное меню':
            self.bot_game.main_menu.start(message)
