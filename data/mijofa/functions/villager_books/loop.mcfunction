execute as @e[type=villager,nbt={Offers:{Recipes:[{sell:{id:"minecraft:enchanted_book"}}]}}] at @s run function mijofa:villager_books/apply_custom_model_data

schedule function mijofa:villager_books/loop 60s
