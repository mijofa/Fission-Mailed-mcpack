# FIXME: Don't bother if it has no enchants
execute as @e[type=minecraft:item] at @s if block ~ ~-0.25 ~ minecraft:smithing_table if entity @s[nbt={Item:{id:"minecraft:diamond_sword"}}] run function mijofa:smithing_fancy/diamond_sword

schedule function mijofa:smithing_fancy/loop 1s
