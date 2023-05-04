# The `data modify` command doesn't support adding/subtracting with NBT tags,
# so we have to use a scoreboard for that part.
scoreboard objectives add FancyCustomModelData dummy

function mijofa:smithing_fancy/loop
