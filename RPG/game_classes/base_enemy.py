from random import randint


class BaseEnemy:
    def __init__(self, name, fight_message, hp, damage, accuracy, perception, luck, agility):
        self.name = name
        self.fight_message = fight_message
        self.hp = hp
        self.damage = damage
        self.accuracy = accuracy
        self.perception = perception
        self.luck = luck
        self.agility = agility

    def attack(self, player, shot_accuracy, shot_damage_coef):
        if randint(0, 19) in range(self.accuracy + shot_accuracy):
            if randint(0, 9) in range(self.luck):
                player.hp -= (self.damage * 3 * shot_damage_coef - player.armor)
                return f'Golpe crítico, {self.name} te hace daño.' \
                       f'daño в {self.damage * 3 * shot_damage_coef - player.armor} hp'
            else:
                player.hp -= (self.damage + player.armor)
                return f'¡Golpe! {self.name} te hace daño в {self.damage * shot_damage_coef - player.armor} hp'

        else:
            if randint(0, 9) not in range(self.luck):
                self.hp -= self.damage * shot_damage_coef
                return f'Error crítico! {self.name} se mete en la mano y se propaga' \
                       f' daño в {self.damage * shot_damage_coef} hp'
            return f'{self.name} falla!'
