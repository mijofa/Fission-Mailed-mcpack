# I can't find any way to select only entities where enchanted_book's CustomModelData is unset.
# If it were equal to 0 when unset that would be perfect, but that doesn't seem to be the case.
execute as @e[type=villager,nbt={Offers:{Recipes:[{sell:{id:"minecraft:enchanted_book"}}]}}] at @s run function mijofa:villager_books/apply_custom_model_data

# Given the above issue, I expect this is actually a rather inefficient function, since it runs on every librarian every time.
# So let's just run it once a minute, it's not like I need it to happen instantly anyway.
schedule function mijofa:villager_books/loop 60s
