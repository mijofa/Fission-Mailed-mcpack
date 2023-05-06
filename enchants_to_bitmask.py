"""FIXME."""
import argparse

# 	 Helmet
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	respiration
# 0512	0001000000000	aqua_affinity
# 0256	0000100000000	thorns
# 0128	0000010000000	vanishing_curse
# 0064	0000001000000	protection
# 0032	0000000100000	projectile_protection
# 0016	0000000010000	fire_protection
# 0008	0000000001000	blast_protection
# 	 Turtle Shell
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	respiration
# 0512	0001000000000	aqua_affinity
# 0256	0000100000000	thorns
# 0128	0000010000000	vanishing_curse
# 0064	0000001000000	protection
# 0032	0000000100000	projectile_protection
# 0016	0000000010000	fire_protection
# 0008	0000000001000	blast_protection
# 	 Chestplate
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	thorns
# 0512	0001000000000	vanishing_curse
# 0256	0000100000000	protection
# 0128	0000010000000	projectile_protection
# 0064	0000001000000	fire_protection
# 0032	0000000100000	blast_protection
# 	 Leggings
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	thorns
# 0512	0001000000000	swift_sneak
# 0256	0000100000000	vanishing_curse
# 0128	0000010000000	protection
# 0064	0000001000000	projectile_protection
# 0032	0000000100000	fire_protection
# 0016	0000000010000	blast_protection
# 0008	0000000001000	depth_strider
# 0004	0000000000100	frost_walker
# 	 Boots
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	feather_falling
# 0512	0001000000000	soul_speed
# 0256	0000100000000	thorns
# 0128	0000010000000	vanishing_curse
# 0064	0000001000000	protection
# 0032	0000000100000	projectile_protection
# 0016	0000000010000	fire_protection
# 0008	0000000001000	blast_protection
# 	 Elytra
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	vanishing_curse
# 	 Sword
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	fire_aspect
# 0512	0001000000000	looting
# 0256	0000100000000	knockback
# 0128	0000010000000	sweeping_edge
# 0064	0000001000000	vanishing_curse
# 0032	0000000100000	sharpness
# 0016	0000000010000	smite
# 0008	0000000001000	bane_of_arthropods
# 	 Axe
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	efficiency
# 0512	0001000000000	vanishing_curse
# 0256	0000100000000	sharpness
# 0128	0000010000000	smite
# 0064	0000001000000	bane_of_arthropods
# 0032	0000000100000	fortune
# 0016	0000000010000	silk_touch
# 	 Bow
# 4096	1000000000000	unbreaking
# 2048	0100000000000	power
# 1024	0010000000000	punch
# 0512	0001000000000	flame
# 0256	0000100000000	vanishing_curse
# 0128	0000010000000	infinity
# 0064	0000001000000	mending
# 	 Trident
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	impaling
# 0512	0001000000000	vanishing_curse
# 0256	0000100000000	channeling
# 0128	0000010000000	riptide
# 0064	0000001000000	loyalty
# 	 Crossbow
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	quick_charge
# 0512	0001000000000	vanishing_curse
# 0256	0000100000000	piercing
# 0128	0000010000000	multishot
# 	 Shield
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	vanishing_curse
# 	 Pickaxe
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	efficiency
# 0512	0001000000000	vanishing_curse
# 0256	0000100000000	fortune
# 0128	0000010000000	silk_touch
# 	 Shovel
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	efficiency
# 0512	0001000000000	vanishing_curse
# 0256	0000100000000	fortune
# 0128	0000010000000	silk_touch
# 	 Hoe
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	efficiency
# 0512	0001000000000	vanishing_curse
# 0256	0000100000000	fortune
# 0128	0000010000000	silk_touch
# 	 Fishing Rod
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	lure
# 0512	0001000000000	luck_of_the_sea
# 0256	0000100000000	vanishing_curse
# 	 Shears
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	efficiency
# 0512	0001000000000	vanishing_curse
# 	 Flint and Steel
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	vanishing_curse
# 	 Carrot on a Stick
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	vanishing_curse
# 	 Warped Fungus on a Stick
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	vanishing_curse
# 	 Brush
# 4096	1000000000000	mending
# 2048	0100000000000	unbreaking
# 1024	0010000000000	vanishing_curse
# 	 Compass
# 4096	1000000000000	vanishing_curse
# 	 Recovery Compass
# 4096	1000000000000	vanishing_curse
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
    "brush": {
        "mending": 0b1000000000000,
        "unbreaking": 0b0100000000000,
        "vanishing_curse": 0b0010000000000,
    },
    "carrot_on_a_stick": {
        "mending": 0b1000000000000,
        "unbreaking": 0b0100000000000,
        "vanishing_curse": 0b0010000000000,
    },
    "flint_and_steel": {
        "mending": 0b1000000000000,
        "unbreaking": 0b0100000000000,
        "vanishing_curse": 0b0010000000000,
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
    "shears": {
        "efficiency": 0b1000000000000,
        "mending": 0b0100000000000,
        "unbreaking": 0b0010000000000,
        "vanishing_curse": 0b0001000000000,
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
    "warped_fungus_on_a_stick": {
        "mending": 0b1000000000000,
        "unbreaking": 0b0100000000000,
        "vanishing_curse": 0b0010000000000,
    },
    "bow": {
        "flame": 0b1000000000000,
        "infinity": 0b0100000000000,
        "mending": 0b0010000000000,
        "power": 0b0001000000000,
        "punch": 0b0000100000000,
        "unbreaking": 0b0000010000000,
        "vanishing_curse": 0b0000001000000,
    },
    # # FIXME: These all have multiple stages of texture for action animations, supportable, but requires a little more effort.
    # # NOTE: I did so for bows, but they're far more common, and mostly "just worked" these seem a little more complex... maybe
    # "crossbow": {
    #     "mending": 0b1000000000000,
    #     "multishot": 0b0100000000000,
    #     "piercing": 0b0010000000000,
    #     "quick_charge": 0b0001000000000,
    #     "unbreaking": 0b0000100000000,
    #     "vanishing_curse": 0b0000010000000,
    # },
    # "shield": {
    #     "mending": 0b1000000000000,
    #     "unbreaking": 0b0100000000000,
    #     "vanishing_curse": 0b0010000000000,
    # },
    # "fishing_rod": {
    #     "luck_of_the_sea": 0b1000000000000,
    #     "lure": 0b0100000000000,
    #     "mending": 0b0010000000000,
    #     "unbreaking": 0b0001000000000,
    #     "vanishing_curse": 0b0000100000000,
    # },
    # # NOTE: Compasses sound like a hell of a lot of animation frames, not important enough to bother with that effort.
    # "compass": {
    #     "vanishing_curse": 0b1000000000000,
    # },
    # "recovery_compass": {
    #     "vanishing_curse": 0b1000000000000,
    # },
    # FIXME: I'm not sure why Tridents are complex, but they look to be
    # "trident": {
    #     "channeling": 0b1000000000000,
    #     "impaling": 0b0100000000000,
    #     "loyalty": 0b0010000000000,
    #     "mending": 0b0001000000000,
    #     "riptide": 0b0000100000000,
    #     "unbreaking": 0b0000010000000,
    #     "vanishing_curse": 0b0000001000000,
    # },
    # # NOTE: Minecraft doesn't support CustomModelData for the **worn** 3D model, so I'm not bothering to support them for now.
    # #       It would still be useful to identify them in chests/etc though, so maybe at a future date.
    # # FIXME: Wait, why is there no binding_curse in this list?
    # "helmet": {
    #     "aqua_affinity": 0b1000000000000,
    #     "blast_protection": 0b0100000000000,
    #     "fire_protection": 0b0010000000000,
    #     "mending": 0b0001000000000,
    #     "projectile_protection": 0b0000100000000,
    #     "protection": 0b0000010000000,
    #     "respiration": 0b0000001000000,
    #     "thorns": 0b0000000100000,
    #     "unbreaking": 0b0000000010000,
    #     "vanishing_curse": 0b0000000001000,
    # },
    # "turtle_shell": {
    #     "aqua_affinity": 0b1000000000000,
    #     "blast_protection": 0b0100000000000,
    #     "fire_protection": 0b0010000000000,
    #     "mending": 0b0001000000000,
    #     "projectile_protection": 0b0000100000000,
    #     "protection": 0b0000010000000,
    #     "respiration": 0b0000001000000,
    #     "thorns": 0b0000000100000,
    #     "unbreaking": 0b0000000010000,
    #     "vanishing_curse": 0b0000000001000,
    # },
    # "pumpkin": {
    #     "binding_curse": 0b1000000000000,
    #     "vanishing_curse": 0b0100000000000,
    # },
    # "chestplate": {
    #     "blast_protection": 0b1000000000000,
    #     "fire_protection": 0b0100000000000,
    #     "mending": 0b0010000000000,
    #     "projectile_protection": 0b0001000000000,
    #     "protection": 0b0000100000000,
    #     "thorns": 0b0000010000000,
    #     "unbreaking": 0b0000001000000,
    #     "vanishing_curse": 0b0000000100000,
    # },
    # "elytra": {
    #     "mending": 0b1000000000000,
    #     "unbreaking": 0b0100000000000,
    #     "vanishing_curse": 0b0010000000000,
    # },
    # "leggings": {
    #     "blast_protection": 0b1000000000000,
    #     "depth_strider": 0b0100000000000,
    #     "fire_protection": 0b0010000000000,
    #     "frost_walker": 0b0001000000000,
    #     "mending": 0b0000100000000,
    #     "projectile_protection": 0b0000010000000,
    #     "protection": 0b0000001000000,
    #     "swift_sneak": 0b0000000100000,
    #     "thorns": 0b0000000010000,
    #     "unbreaking": 0b0000000001000,
    #     "vanishing_curse": 0b0000000000100,
    # },
    # "boots": {
    #     "blast_protection": 0b1000000000000,
    #     "feather_falling": 0b0100000000000,
    #     "fire_protection": 0b0010000000000,
    #     "mending": 0b0001000000000,
    #     "projectile_protection": 0b0000100000000,
    #     "protection": 0b0000010000000,
    #     "soul_speed": 0b0000001000000,
    #     "thorns": 0b0000000100000,
    #     "unbreaking": 0b0000000010000,
    #     "vanishing_curse": 0b0000000001000,
    # },
}

# FIXME: Only some things can have prefixes, and we don't check that at all
prefixes = ['leather_', 'wooden_', 'stone_', 'golden_', 'iron_', 'diamond_', 'netherite_']

parser = argparse.ArgumentParser()
parser.add_argument('item_name', type=str)
parser.add_argument('enchantments', nargs='+', type=str)

args = parser.parse_args()

if args.item_name.startswith('bow_pulling_'):
    item_bits = item_enchant_bitmasks['bow']
elif args.item_name in item_enchant_bitmasks:
    item_bits = item_enchant_bitmasks[args.item_name]
elif '_' in args.item_name and args.item_name.split('_', maxsplit=1)[1] in item_enchant_bitmasks:
    assert any((True for p in prefixes if args.item_name.startswith(p))), f"Prefix not found for item ({args.item_name})"
    item_bits = item_enchant_bitmasks[args.item_name.split('_', maxsplit=1)[1]]
else:
    raise Exception(f"Item ({args.item_name}) not found")

enchantment_aliases = {'vanishing': 'vanishing_curse', 'bane': 'bane_of_arthropods', 'sweeping': 'sweeping_edge'}

output = 0b0
for ench in args.enchantments:

    if ench in enchantment_aliases:
        ench = enchantment_aliases[ench]

    assert ench in item_bits, f"Enchantment ({ench}) not found. Incompatible with item(args.item_name)?"
    output = output | item_bits[ench]

# Since 'output' is still I need to do this formatting conversion to display it in binary, just to make it easier to ready later
print(f'{args.item_name}/0b{output:013b}')
