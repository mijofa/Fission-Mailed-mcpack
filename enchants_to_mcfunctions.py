"""FIXME."""
import pathlib

# FIXME: This is copied straight from enchants_to_bitmasks.py, combine those files or make a library
item_enchant_bitmasks = {
    "axe": {
        "bane_of_arthropods": 0b1000000000000,
        "efficiency": 0b0100000000000,
        "fortune": 0b0010000000000,
        "mending": 0b0001000000000,
        "sharpness": 0b0000100000000,
        "silk_touch": 0b0000010000000,
        "smite": 0b0000001000000,
        "unbreaking": 0b0000000100000,
        "vanishing_curse": 0b0000000010000,
    },
    "hoe": {
        "efficiency": 0b1000000000000,
        "fortune": 0b0100000000000,
        "mending": 0b0010000000000,
        "silk_touch": 0b0001000000000,
        "unbreaking": 0b0000100000000,
        "vanishing_curse": 0b0000010000000,
    },
    "pickaxe": {
        "efficiency": 0b1000000000000,
        "fortune": 0b0100000000000,
        "mending": 0b0010000000000,
        "silk_touch": 0b0001000000000,
        "unbreaking": 0b0000100000000,
        "vanishing_curse": 0b0000010000000,
    },
    "shovel": {
        "efficiency": 0b1000000000000,
        "fortune": 0b0100000000000,
        "mending": 0b0010000000000,
        "silk_touch": 0b0001000000000,
        "unbreaking": 0b0000100000000,
        "vanishing_curse": 0b0000010000000,
    },
    "sword": {
        "bane_of_arthropods": 0b1000000000000,
        "fire_aspect": 0b0100000000000,
        "knockback": 0b0010000000000,
        "looting": 0b0001000000000,
        "mending": 0b0000100000000,
        "sharpness": 0b0000010000000,
        "smite": 0b0000001000000,
        "sweeping_edge": 0b0000000100000,
        "unbreaking": 0b0000000010000,
        "vanishing_curse": 0b0000000001000,
    },
    "bow": {
        "flame": 0b1000000000000,
        "infinity": 0b0100000000000,
        "mending": 0b0010000000000,
        "power": 0b0001000000000,
        "punch": 0b0000100000000,
        "unbreaking": 0b0000010000000,
        "vanishing_curse": 0b0000001000000,
    }
}

functions_path = pathlib.Path('data/mijofa/functions/smithing_fancy/')

for item in item_enchant_bitmasks:
    with (functions_path / f'{item}.mcfunction').open('w') as f:
        for enchant in item_enchant_bitmasks[item]:
            print('execute if entity @s[nbt={Item:{tag:{Enchantments:[{id:"minecraft:', enchant, '"}]}}}]'
                  ' run scoreboard players add @s FancyCustomModelData ', item_enchant_bitmasks[item][enchant],
                  sep='', file=f, flush=True)
