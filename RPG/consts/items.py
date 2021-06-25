from RPG.game_classes.items.base_weapon import BaseWeapon
from RPG.game_classes.items.medpack import MedPack
from RPG.game_classes.items.base_armor import BaseArmorSet

LITTLE_MED_PACK = MedPack('Pequeño paquete médico', 10)

LIGHT_SOLDIER_ARMOR_SET = BaseArmorSet('Armadura de soldado ligero', 10, 700)

LIGHT_LASER_RIFFLE = BaseWeapon('Rifle láser ligero', 10, 3, 5, 500)
OLD_LASER_PISTOL = BaseWeapon('Pistola láser desgastada', 12, 4, 7, 100)

items = {'medpak': LITTLE_MED_PACK, 'armadura': LIGHT_SOLDIER_ARMOR_SET, 'rifle': LIGHT_LASER_RIFFLE,
         'pistola': OLD_LASER_PISTOL, '': None}
