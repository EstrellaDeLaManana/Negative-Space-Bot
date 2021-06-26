from random import randint
from RPG.consts.items import items


class Player:
    def __init__(self, name):
        self.name = name  # Características principales del jugador
        self.hp = 60
        self.armor = 0
        self.level = 1
        self.money = 250

        self.endurance = 1  # Parámetros individuales del jugador
        self.accuracy = 6
        self.perception = 1
        self.charisma = 1
        self.agility = 1
        self.luck = 4

        self.quest_items = []  # Lista de objetos de búsqueda recibidos

        self.inventory = [None] * 5  # Inventario y equipo
        self.weapon = None
        self.armor_set = None
        self.laser_ammo = 0

        self.in_fight = False  # Si el jugador está en combate

    def get_stats(self):
        stats = f'*{self.name}* 😎\n' \
                f'🎖 _Nivel_: {self.level}\n' \
                f'❤ _Salud_: {self.hp}\n' \
                f'💵 _Préstamos_: {self.money}\n' \
                f'*Características*\n' \
                f'🔫 _Precisión_: {self.accuracy}\n' \
                f'👂🏻 _Percepción_: {self.perception}\n' \
                f'🏃🏻‍♂ _Resistencia_: {self.endurance}\n' \
                f'🗣 _Carisma_: {self.charisma}\n' \
                f'🏃🏻‍♂ _Agilidad_: {self.agility}\n' \
                f'🍀 _Suerte_: {self.luck}'
        return stats

    def add_item(self, item):
        added_item = False
        for i in range(len(self.inventory)):
            if self.inventory[i] is None:
                self.inventory[i] = item
                added_item = True
                break
        return added_item

    def buy_item(self, item, trader_factor):
        if self.money >= item.price:
            if not self.add_item(item):
                return False, 'el inventario está lleno'
            else:
                self.money -= int(item.price * trader_factor)
                return True, 'Comprado con éxito:'
        else:
            return False, 'no hay suficiente dinero'

    def sell_item(self, item, trader_factor):
        self.money += int(item.price / trader_factor)
        self.inventory.remove(item)

    def drop_item(self, item):
        self.inventory[self.inventory.index(item)] = None
        self.sort_inventory()

    def sort_inventory(self):
        for i in range(len(self.inventory)):
            if i != 0:
                if self.inventory[i - 1] is None:
                    self.inventory[i - 1] = self.inventory[i]
                    self.inventory[i] = None

    def get_equipment(self):
        weapon, armor_set = self.weapon, self.armor_set
        if self.weapon is None:
            weapon = ' <Está vacío>'
        if self.armor_set is None:
            armor_set = ' <Está vacío>'
        equipment = f'😎 *{self.name}*\n' \
                    f'🧥 _Kit de armadura_: {str(armor_set)[1:]}\n' \
                    f'🔫 _Armas_: {str(weapon)[1:]}\n' \
                    f'🔋 _Láser_: {self.laser_ammo}'
        return equipment

    def attack(self, enemy, shot_accuracy, shot_damage_coef):
        if randint(0, 19) in range(self.accuracy + shot_accuracy):
            if randint(0, 9) in range(self.luck):
                enemy.hp -= self.weapon.damage * 3
                return f'Golpe crítico, golpeas al enemigo ' \
                       f'daño en {self.weapon.damage * 3 * shot_damage_coef} hp'
            else:
                enemy.hp -= self.weapon.damage * shot_damage_coef
                return f'¡Golpe! Haz daño al enemigo en {self.weapon.damage * shot_damage_coef} hp'

        else:
            if randint(0, 9) not in range(self.luck):
                self.hp -= self.weapon.damage
                return f'Error crítico! Te caes ' \
                       f'a TI mismo en el pie y hacer daño en el Tamaño {self.weapon.damage * shot_damage_coef} hp'
            return 'Tiro perdido!'

    def inventory_to_str(self):
        inventory = []
        for item in self.inventory:
            if item is not None:
                for item_name in items:
                    if items[item_name] == item:
                        inventory.append(item_name)
        return ', '.join(inventory)

    def weapon_to_str(self):
        weapon_name = None
        for item_name in items:
            if items[item_name] == self.weapon:
                weapon_name = item_name
        return weapon_name

    def armor_to_str(self):
        armor_name = None
        for item_name in items:
            if items[item_name] == self.armor_set:
                armor_name = item_name
        return armor_name
