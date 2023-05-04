# This will probably need to use a scoreboard to do the CustomModelData calculations to get what we want.
# Refer to custom_roleplay_data datapack.
# The `data modify` command doesn't support adding/subtracting from the CustomModelData,
# in fact I'm pretty sure it's entire logic is string based anyway.
# Using a scoreboard like custom_roleplay_data does might make all that easier.
say "Will need to do a thing here"

# Show some particles on it to indicate we've actually done something
particle minecraft:enchant ~ ~0.5 ~ 0.1 0.25 0.1 0 15
