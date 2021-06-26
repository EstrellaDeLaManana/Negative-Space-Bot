from time import sleep
from datetime import datetime
from RPG.consts.game_states import COMPUTER
from RPG.bot_classes.base_handler import BaseHandler


class Computer(BaseHandler):
    def __init__(self, game, spaceship):
        super().__init__(game, COMPUTER)
        self.spaceship = spaceship

    def show(self, message):
        self.game.bot.send_message(message.chat.id, "Te acercas a la computadora de a bordo y la ejecutas")
        sleep(1)
        self.game.bot.send_message(message.chat.id, "_Spaceship Minisoft console: starting._",
                                   parse_mode='Markdown')
        sleep(1)
        self.game.bot.send_message(message.chat.id, "_Loading..._",
                                   parse_mode='Markdown')
        sleep(2)
        self.game.bot.send_message(message.chat.id,
                                   f"_Spaceship Minisoft console 3.8.2 _ {str(datetime.today())[:-7]}",
                                   parse_mode='Markdown')
        self.game.bot.send_message(message.chat.id, '_ Ingrese "help" para obtener una lista de los fundamentos de los comandos_',
                                   parse_mode='Markdown')

    def handle(self, message):
        if message.text == 'help':
            self.game.bot.send_message(message.chat.id,
                                       '*srp < nombre del PLANETA> * _ - establecer la ruta al planeta seleccionado_ \n'
                                       '*sps inf eqp * _ - ver información sobre el barco y su equipo_ \n'
                                       '*IPC < nombre del PLANETA> * _ - ver información sobre el planeta_ \n'
                                       '*pln * _ - muestra una lista de los planetas más cercanos_ \n'
                                       '*plo * _ - sacar la espina de los planetas abiertos_ \n'
                                       '*q * _ - cerrar la consola Spaceship Minisoft_',
                                       parse_mode='Markdown')
        elif message.text.startswith('srp'):
            planet_name = message.text[4:].strip().capitalize()
            for planet in self.game.planets:
                if planet.name == planet_name:
                    self.game.current_planet = planet
                    self.game.bot.send_message(message.chat.id, f'Has llegado con éxito al planeta {planet_name}')
                    if planet not in self.game.opened_planets:
                        self.game.opened_planets.append(planet)
                else:
                    self.game.bot.send_message(message.chat.id, 'Es imposible obtener una ruta a este planeta. '
                                                                'Causa: planeta no encontrado')
        elif message.text.strip() == 'sps inf eqp':
            self.game.bot.send_message(message.chat.id, self.spaceship.get_info(), parse_mode='Markdown')
        elif message.text.startswith('cpi'):
            planet_name = message.text[4:].strip().capitalize()
            for planet in self.game.planets:
                if planet.name == planet_name:
                    self.game.bot.send_message(message.chat.id, planet.get_info(),
                                               parse_mode='Markdown')
                else:
                    self.game.bot.send_message(message.chat.id, 'No se pudo encontrar información sobre este planeta.')
        elif message.text.strip() == 'pln':  # TODO other planets
            if not self.game.current_planet:
                self.game.bot.send_message(message.chat.id, '🌎 * Planetas cercanos*\n'
                                                            '       - Tablados',
                                           parse_mode='Markdown')
        elif message.text.strip() == 'plo':
            if self.game.opened_planets:
                opened_planets = '      -' + '\n      - '.join([str(planet) for planet in self.game.opened_planets])
                self.game.bot.send_message(message.chat.id, f'🌎Planetas abiertos\n'
                                                            f'{opened_planets}')
            else:
                self.game.bot.send_message(message.chat.id, 'Aún no has descubierto ningún planeta.',
                                           parse_mode='Markdown')
        elif message.text == 'q':
            self.game.bot.send_message(message.chat.id, '_Closing terminal..._',
                                       parse_mode='Markdown')
            sleep(1)
            self.game.bot.send_message(message.chat.id, '_Process finished with exit code -1_',
                                       parse_mode='Markdown')
            sleep(1)
            self.spaceship.captain_bridge.start(message)
        else:
            self.game.bot.send_message(message.chat.id, 'Se ha introducido un comando desconocido. Inténtalo de nuevo.')
