from telebot.types import ReplyKeyboardMarkup
from RPG.game_states import CAPTAIN_BRIDGE
from RPG.bot_classes.locations.base_location import BaseLocation


class CaptainBridge(BaseLocation):
    def __init__(self, bot_game, spaceship):
        super().__init__(bot_game, CAPTAIN_BRIDGE, 'Капитанский мостик', 'Ты выходишь на капитанский мостик, '
                                                                         'по всюду виднеются различные элементы '
                                                                         'управления кораблём. В большой панорамный '
                                                                         'иллюминатор открыватеся вид на галактику. На '
                                                                         'главной панели управления ты видишь '
                                                                         'интерфейс управления бортовым компьютером')
        self.spaceship = spaceship
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)
        self.reply_keyboard.row('📟Бортовой компьютер', '🛏Личная каюта')
        self.reply_keyboard.row('📦Грузовой отсек', '📟Главное меню')

    def handle(self, message):
        if message.text == '📟Бортовой компьютер':
            pass
        elif message.text == '🛏Личная каюта':
            self.spaceship.cabin.start(message)
        elif message.text == '📦Грузовой отсек':
            self.spaceship.cargo_hold.start(message)
        elif message.text == '📟Главное меню':
            self.bot_game.main_menu.start(message)
        else:
            self.show_input_error(message)
