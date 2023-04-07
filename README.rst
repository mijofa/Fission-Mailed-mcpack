Mostly combining a few packs:

* `Armoured Elytra <https://www.planetminecraft.com/texture-pack/armoured-elytra-resource-pack-for-vanillatweaks-datapack/>`_
* `Minimal Armour <https://www.planetminecraft.com/texture-pack/minimal-armor/>`_
  FIXME: 1.20 will bring in armour trims, which will likely make this one a mess. If possible simply don't apply it to trimmed armour, since you want to show off the armour at that point, rather than your player skin
* `Prosperity Resource Pack <https://github.com/ProsperityMC/Prosperity-Resource-Pack>`_ (Totems only)
  FIXME: I'd like the hats/pumpkins, but it wasn't working without Optifine
* `Fancy Beds <https://modrinth.com/resourcepack/fancy-beds>`_

Along with some hacks to allow me to flex some `Visual Enchantments <https://github.com/CiscuLog/Visual-Enchantments>`_ using CustomModelData without making other players/friends install Optifine/CITResewn

You can apply these textures using the `Custom Roleplay Data <https://www.curseforge.com/minecraft/customization/custom-roleplay-data-datapack>`_ datapack (installed on Fission Mailed server) by holding the associated item in your main hand, then putting ``/trigger CustomModelData set <ID>`` with the custom model ID in the chat

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
These are based on CiscuLog's `Visual Enchantments <https://github.com/CiscuLog/Visual-Enchantments>`_ pack, which otherwise depends on Optifine/CITResewn

Longer term I'd love to have a datapack that automatically applies custom model data according to a bitmask of applied enchantments.
Might require the player to drop the item on a smithing table or something to apply that data rather than as part of the crafting recipes.
I don't really know about making my own datapacks though, and what I have investigated they don't seem very server resource efficient.

For now I'm just manually creating custom model definitions for each of my own tools as I decide to update the pack.
This is the table of those IDs, without thumbnails because I CBFed generating those layered images.

I'm happy to add more on request, just tell me the tool and the list of enchantments (the level is irrelevant) and I'll update the pack.
The IDs might change at a future date, although mijofa has personally registered the #645xxxx prefix at the unofficial `Minecraft Datapacks <https://mcdatapack.vercel.app/>`_, so the prefix shouldn't change, and hopefully won't conflict with others.

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
This is mostly just to make villager trading halls look a bit better,
by putting fancy looking books above each trading module to indicate what they're selling.

It will have zero impact on the look of the books being sold,
but it does make it much easier to keep track of which villager is which.

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
