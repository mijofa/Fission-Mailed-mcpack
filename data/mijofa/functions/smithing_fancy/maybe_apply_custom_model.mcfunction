scoreboard players set @s FancyCustomModelData 6450000


execute if entity @s[nbt={Item:{id:"minecraft:wooden_axe"}}] run function mijofa:smithing_fancy/axe
execute if entity @s[nbt={Item:{id:"minecraft:wooden_pickaxe"}}] run function mijofa:smithing_fancy/pickaxe
execute if entity @s[nbt={Item:{id:"minecraft:wooden_shovel"}}] run function mijofa:smithing_fancy/shovel
execute if entity @s[nbt={Item:{id:"minecraft:wooden_sword"}}] run function mijofa:smithing_fancy/sword
execute if entity @s[nbt={Item:{id:"minecraft:wooden_hoe"}}] run function mijofa:smithing_fancy/hoe

execute if entity @s[nbt={Item:{id:"minecraft:stone_axe"}}] run function mijofa:smithing_fancy/axe
execute if entity @s[nbt={Item:{id:"minecraft:stone_pickaxe"}}] run function mijofa:smithing_fancy/pickaxe
execute if entity @s[nbt={Item:{id:"minecraft:stone_shovel"}}] run function mijofa:smithing_fancy/shovel
execute if entity @s[nbt={Item:{id:"minecraft:stone_sword"}}] run function mijofa:smithing_fancy/sword
execute if entity @s[nbt={Item:{id:"minecraft:stone_hoe"}}] run function mijofa:smithing_fancy/hoe

execute if entity @s[nbt={Item:{id:"minecraft:iron_axe"}}] run function mijofa:smithing_fancy/axe
execute if entity @s[nbt={Item:{id:"minecraft:iron_pickaxe"}}] run function mijofa:smithing_fancy/pickaxe
execute if entity @s[nbt={Item:{id:"minecraft:iron_shovel"}}] run function mijofa:smithing_fancy/shovel
execute if entity @s[nbt={Item:{id:"minecraft:iron_sword"}}] run function mijofa:smithing_fancy/sword
execute if entity @s[nbt={Item:{id:"minecraft:iron_hoe"}}] run function mijofa:smithing_fancy/hoe

execute if entity @s[nbt={Item:{id:"minecraft:golden_axe"}}] run function mijofa:smithing_fancy/axe
execute if entity @s[nbt={Item:{id:"minecraft:golden_pickaxe"}}] run function mijofa:smithing_fancy/pickaxe
execute if entity @s[nbt={Item:{id:"minecraft:golden_shovel"}}] run function mijofa:smithing_fancy/shovel
execute if entity @s[nbt={Item:{id:"minecraft:golden_sword"}}] run function mijofa:smithing_fancy/sword
execute if entity @s[nbt={Item:{id:"minecraft:golden_hoe"}}] run function mijofa:smithing_fancy/hoe

execute if entity @s[nbt={Item:{id:"minecraft:diamond_axe"}}] run function mijofa:smithing_fancy/axe
execute if entity @s[nbt={Item:{id:"minecraft:diamond_pickaxe"}}] run function mijofa:smithing_fancy/pickaxe
execute if entity @s[nbt={Item:{id:"minecraft:diamond_shovel"}}] run function mijofa:smithing_fancy/shovel
execute if entity @s[nbt={Item:{id:"minecraft:diamond_sword"}}] run function mijofa:smithing_fancy/sword
execute if entity @s[nbt={Item:{id:"minecraft:diamond_hoe"}}] run function mijofa:smithing_fancy/hoe

execute if entity @s[nbt={Item:{id:"minecraft:netherite_axe"}}] run function mijofa:smithing_fancy/axe
execute if entity @s[nbt={Item:{id:"minecraft:netherite_pickaxe"}}] run function mijofa:smithing_fancy/pickaxe
execute if entity @s[nbt={Item:{id:"minecraft:netherite_shovel"}}] run function mijofa:smithing_fancy/shovel
execute if entity @s[nbt={Item:{id:"minecraft:netherite_sword"}}] run function mijofa:smithing_fancy/sword
execute if entity @s[nbt={Item:{id:"minecraft:netherite_hoe"}}] run function mijofa:smithing_fancy/hoe

execute if entity @s[nbt={Item:{id:"minecraft:bow"}}] run function mijofa:smithing_fancy/bow


execute store result entity @s Item.tag.CustomModelData int 1.0 run scoreboard players get @s FancyCustomModelData
# Show some particles on it to indicate we've actually done something
particle minecraft:enchant ~ ~0.5 ~ 0.1 0.25 0.1 0 15
