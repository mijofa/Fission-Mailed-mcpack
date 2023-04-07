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

======================  ========  ======================================================================================
Enchantment             ID        Icon
======================  ========  ======================================================================================
Aqua Affinity           6453001   .. image:: assets/minecraft/textures/item/books/aqua_affinity.png
                                     :width: 32
Bane of Arthropods      6453002   .. image:: assets/minecraft/textures/item/books/bane_of_arthropods.png
                                     :width: 32
Blast Protection        6453003   .. image:: assets/minecraft/textures/item/books/blast_protection.png
                                     :width: 32
Channeling              6453004   .. image:: assets/minecraft/textures/item/books/channeling.png
                                     :width: 32
Chopping                6453005   .. image:: assets/minecraft/textures/item/books/chopping.png
                                     :width: 32
Curse of Binding        6453006   .. image:: assets/minecraft/textures/item/books/curse_of_binding.png
                                     :width: 32
Curse of Vanishing      6453007   .. image:: assets/minecraft/textures/item/books/curse_of_vanishing.png
                                     :width: 32
Depth Strider           6453008   .. image:: assets/minecraft/textures/item/books/depth_strider.png
                                     :width: 32
Efficiency              6453009   .. image:: assets/minecraft/textures/item/books/efficiency.png
                                     :width: 32
Feather Falling         6453010   .. image:: assets/minecraft/textures/item/books/feather_falling.png
                                     :width: 32
Fire Aspect             6453011   .. image:: assets/minecraft/textures/item/books/fire_aspect.png
                                     :width: 32
Fire Protection         6453012   .. image:: assets/minecraft/textures/item/books/fire_protection.png
                                     :width: 32
Flame                   6453013   .. image:: assets/minecraft/textures/item/books/flame.png
                                     :width: 32
Fortune                 6453014   .. image:: assets/minecraft/textures/item/books/fortune.png
                                     :width: 32
Frost Walker            6453015   .. image:: assets/minecraft/textures/item/books/frost_walker.png
                                     :width: 32
Impaling                6453016   .. image:: assets/minecraft/textures/item/books/impaling.png
                                     :width: 32
Infinity                6453017   .. image:: assets/minecraft/textures/item/books/infinity.png
                                     :width: 32
Knockback               6453018   .. image:: assets/minecraft/textures/item/books/knockback.png
                                     :width: 32
Looting                 6453019   .. image:: assets/minecraft/textures/item/books/looting.png
                                     :width: 32
Loyalty                 6453020   .. image:: assets/minecraft/textures/item/books/loyalty.png
                                     :width: 32
Luck of The Sea         6453021   .. image:: assets/minecraft/textures/item/books/luck_of_the_sea.png
                                     :width: 32
Lure                    6453022   .. image:: assets/minecraft/textures/item/books/lure.png
                                     :width: 32
Mending                 6453023   .. image:: assets/minecraft/textures/item/books/mending.png
                                     :width: 32
Multishot               6453024   .. image:: assets/minecraft/textures/item/books/multishot.png
                                     :width: 32
Piercing                6453025   .. image:: assets/minecraft/textures/item/books/piercing.png
                                     :width: 32
Power                   6453026   .. image:: assets/minecraft/textures/item/books/power.png
                                     :width: 32
Projectile Protection   6453027   .. image:: assets/minecraft/textures/item/books/projectile_protection.png
                                     :width: 32
Protection              6453028   .. image:: assets/minecraft/textures/item/books/protection.png
                                     :width: 32
Punch                   6453029   .. image:: assets/minecraft/textures/item/books/punch.png
                                     :width: 32
Quick Charge            6453030   .. image:: assets/minecraft/textures/item/books/quick_charge.png
                                     :width: 32
Respiration             6453031   .. image:: assets/minecraft/textures/item/books/respiration.png
                                     :width: 32
Riptide                 6453032   .. image:: assets/minecraft/textures/item/books/riptide.png
                                     :width: 32
Sharpness               6453033   .. image:: assets/minecraft/textures/item/books/sharpness.png
                                     :width: 32
Silk Touch              6453034   .. image:: assets/minecraft/textures/item/books/silk_touch.png
                                     :width: 32
Smite                   6453035   .. image:: assets/minecraft/textures/item/books/smite.png
                                     :width: 32
Soul Speed              6453036   .. image:: assets/minecraft/textures/item/books/soul_speed.png
                                     :width: 32
Sweeping Edge           6453037   .. image:: assets/minecraft/textures/item/books/sweeping_edge.png
                                     :width: 32
Swift Sneak             6453038   .. image:: assets/minecraft/textures/item/books/swift_sneak.png
                                     :width: 32
Thorns                  6453039   .. image:: assets/minecraft/textures/item/books/thorns.png
                                     :width: 32
Unbreaking              6453040   .. image:: assets/minecraft/textures/item/books/unbreaking.png
                                     :width: 32
======================  ========  ======================================================================================

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
