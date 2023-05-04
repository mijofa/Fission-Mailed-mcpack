# If there is an enchanted item on a smithing table, run the maybe_apply... function.
execute as @e[type=minecraft:item] at @s if block ~ ~-0.25 ~ minecraft:smithing_table if entity @s[nbt={Item:{tag:{Enchantments:[{}]}}}] run function mijofa:smithing_fancy/maybe_apply_custom_model

schedule function mijofa:smithing_fancy/loop 1s
