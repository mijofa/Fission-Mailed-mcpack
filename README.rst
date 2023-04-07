Mostly combining a few packs:

* `Armoured Elytra <https://www.planetminecraft.com/texture-pack/armoured-elytra-resource-pack-for-vanillatweaks-datapack/>`_
* `Minimal Armour <https://www.planetminecraft.com/texture-pack/minimal-armor/>`_
* `Prosperity Resource Pack <https://github.com/ProsperityMC/Prosperity-Resource-Pack>`_ (Totems only)
  FIXME: I'd like the hats/pumpkins, but it wasn't working without Optifine
* `Fancy Beds <https://modrinth.com/resourcepack/fancy-beds>`_

Along with some hacks to allow me to flex some `Visual Enchantments <https://github.com/CiscuLog/Visual-Enchantments>`_ using CustomModelData without making other players/friends install Optifine/CITResewn

Custom totems
-------------

====================  ========  ======================================================================================
Item                  ID        Icon
====================  ========  ======================================================================================
Totem of Undying      94560     .. image:: assets/minecraft/textures/item/totem_of_undying/axolotl_of_undying.png
                                   :width: 32
                                   :alt: Axolotl of Undying
Totem of Undying      94561     .. image:: assets/minecraft/textures/item/totem_of_undying/book_of_undying.png
                                   :width: 32
                                   :alt: Book of Undying
Totem of Undying      94562     .. image:: assets/minecraft/textures/item/totem_of_undying/carbon_totem_0.png
                                   :width: 32
                                   :alt: Carbon Totem
Totem of Undying      94563     .. image:: assets/minecraft/textures/item/totem_of_undying/carbon_totem_1.png
                                   :width: 32
                                   :alt: Carbon Totem (Nether)
Totem of Undying      94564     .. image:: assets/minecraft/textures/item/totem_of_undying/diamond_netherite_totem.png
                                   :width: 32
                                   :alt: Netherite Totem (Diamond)
Totem of Undying      94565     .. image:: assets/minecraft/textures/item/totem_of_undying/gold_netherite_totem.png
                                   :width: 32
                                   :alt: Netherite Totem (Gold)
Totem of Undying      94566     .. image:: assets/minecraft/textures/item/totem_of_undying/fancy_totem_of_undying.png
                                   :width: 32
                                   :alt: Fancy Totem of Undying
Totem of Undying      94567     .. image:: assets/minecraft/textures/item/totem_of_undying/flower_of_undying.png
                                   :width: 32
                                   :alt: Flower of Undying
Totem of Undying      94568     .. image:: assets/minecraft/textures/item/totem_of_undying/potion_of_undying.png
                                   :width: 32
                                   :alt: Potion of Undying
Totem of Undying      94569     .. image:: assets/minecraft/textures/item/totem_of_undying/retro_totem_of_undying.png
                                   :width: 32
                                   :alt: Retro Totem of Undying
Totem of Undying      945610    .. image:: assets/minecraft/textures/item/totem_of_undying/small_totem_of_undying.png
                                   :width: 32
                                   :alt: Small Totem of Undying
Totem of Undying      945611    .. image:: assets/minecraft/textures/item/totem_of_undying/totem_of_redstone.png
                                   :width: 32
                                   :alt: Totem of Redstone
Totem of Undying      945612    .. image:: assets/minecraft/textures/item/totem_of_undying/soul_totem.png
                                   :width: 32
                                   :alt: Soul Totem
Totem of Undying      6453000   .. image:: assets/minecraft/textures/item/totem_of_undying/6453000.png
                                   :width: 32
                                   :alt: Mijofa of Undying
Totem of Undying      6453001   .. image:: assets/minecraft/textures/item/totem_of_undying/6453001.png
                                   :width: 32
                                   :alt: Shirtless Mijofa of Undying
====================  ========  ======================================================================================

Visually Enchanted tools
------------------------
Longer term I'd love to have a datapack that automatically applies custom model data according to a bitmask of applied enchantments.
Might require the player to drop the item on a smithing table or something to apply that data instead of as it's being enchanted.
I don't really know what about making my own datapacks though, and what I have investigated they don't seem very server resource efficient.

For now though I'm just manually creating custom model definitions for each of my own tools as I decide to update the pack.
This is the table of those IDs, but I'm not including a thumbnail because I CBFed generating those layered images.

====================  ========  ======================================================================================
Item                  ID        Enchantments
====================  ========  ======================================================================================
Bow                   6453001   * Infinity
                                * Flame
                                * Unbreaking
Diamond Axe           6453001   - Efficiency
                                - Unbreaking
Diamond Pickaxe       6453001   * Silk Touch
                                * Unbreaking
Diamond Shovel        6453001   - Efficiency
                                - Unbreaking
Diamond Sword         6453001   * Knockback
                                * Sharpness
                                * Sweeping Edge
                                * Unbreaking
====================  ========  ======================================================================================

Visually Enchanted Books
------------------------
Not implemented yet

I intend to manually set up a set of custom model data IDs for each visually enchanted book.
Mostly just to make a villager trading hall look a bit better, which fancy looking books above each trading module.
Even though it will have zero impact on the look of the books being sold, it can still be used to visualise what they will sell.

Armoured Elytra
---------------
These IDs are automatically added by Armoured Elytra from `Vanilla Tweaks <https://vanillatweaks.net/picker/datapacks/>`_.
It won't affect the worn model, only the held item (Minecraft doesn't natively custom model data on clothing)

====================  ========  ======================================================================================
Item                  ID        Icon
====================  ========  ======================================================================================
Elytra                13522551  .. image:: assets/minecraft/textures/item/leather_elytra.png
                                   :width: 32
Elytra                13522552  .. image:: assets/minecraft/textures/item/chainmail_elytra.png
                                   :width: 32
Elytra                13522553  .. image:: assets/minecraft/textures/item/golden_elytra.png
                                   :width: 32
Elytra                13522554  .. image:: assets/minecraft/textures/item/iron_elytra.png
                                   :width: 32
Elytra                13522555  .. image:: assets/minecraft/textures/item/diamond_elytra.png
                                   :width: 32
Elytra                13522556  .. image:: assets/minecraft/textures/item/netherite_elytra.png
                                   :width: 32
====================  ========  ======================================================================================
