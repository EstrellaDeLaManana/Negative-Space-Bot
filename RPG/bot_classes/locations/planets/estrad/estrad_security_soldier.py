from RPG.game_states import ESTRAD_SECURITY_SOLDIER
from RPG.bot_classes.base_dialog import BaseDialog


class EstradSecuritySoldier(BaseDialog):
    def __init__(self, game, estrad):
        super().__init__(game, ESTRAD_SECURITY_SOLDIER, 'Солдат Межгалактической Республики',
                         'Приветсвую вас на планете Эстрад, в колонии Межгалактической Республики. Предъявите, '
                         'пожалуйста, ваш пропуск.', '👮🏻‍♂️')
        self.estrad = estrad
        self.reply_keyboard.row('[🗣Харизма 4] Меня прислало высшее руководство передать срочное послание '
                                'вашему начальнику.')
        self.reply_keyboard.row('[💵250] Может можно как-то договориться?')
        self.reply_keyboard.row('Мне уже пора')

    def handle(self, message):
        if message.text == '[🗣Харизма 4] Меня прислало высшее руководство передать срочное послание вашему начальнику.':
            if self.game.players[message.chat.id].charisma >= 4:
                self.say(message, 'Хорошо, проходи.')
            else:
                self.say(message, 'Кого ты пытаешься обмануть? Меня бы предупредили, если'
                                  ' бы начальство кого-то ожидало.')
        elif message.text == '[💵250] Может можно как-то договориться?':
            if self.game.players[message.chat.id].money >= 250:
                self.game.players[message.chat.id].money -= 250
                self.say(message, 'Хорошо, проходи.')
            else:
                self.say(message, 'У тебя и денег то таких нет.')
        elif message.text == 'Мне уже пора':
            self.game.bot.send_message(message.chat.id, 'До встречи.')
            self.estrad.port.start(message)
        else:
            self.show_input_error(message)
