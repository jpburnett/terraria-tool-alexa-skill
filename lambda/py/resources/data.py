# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _

SKILL_NAME = _("Terraria Tool")
WELCOME_MESSAGE = _("Welcome to {}. You can ask me something like, what's the recipe for a {}? \
    Or you can ask me for a random item... Now, what can I help you craft?")

WELCOME_REPROMPT = _("For instructions on what you can say, please say help.")

DISPLAY_CARD_TITLE = _("{}  - Recipe for {}.")

HELP_MESSAGE = _("You can ask, what's the recipe for a {}, or, you can say exit...\
    So, what can I help you craft?")

HELP_REPROMPT = _("You can say things like, what's the recipe for a {}, or you can say exit...\
    So, what can I help you craft?")
    
FALLBACK_MESSAGE = _("The {} skill can't help you with that.")
STOP_MESSAGE = _("Happy Crafting!")
ITEM_REPEAT_MESSAGE = _("Try saying repeat.")
ITEM_NOT_FOUND_MESSAGE = _("I'm sorry, I currently do not know ")
ITEM_NOT_FOUND_WITH_ITEM_NAME = _("the recipe for {}. ")
ITEM_NOT_FOUND_WITHOUT_ITEM_NAME = _("that recipe. ")
ITEM_NOT_FOUND_REPROMPT = _("What else can I help with?")


ITEMS = {
"Iron Pickaxe": "An iron pickaxe can be crafted by using three wood and 12 iron bars at any anvil.", 
"Dirt Block": "Dirt can be dug up from a block on the map",
"Stone Block": "Stone can be mined with a pickaxe throughout the map",
"Iron Broadsword": "An iron broadsword can be crafted by using 8 iron bars at any anvil.",
"Mushroom": "Mushrooms can be found on the surface of the map",
"Iron Shortsword": "made is 7 iron bars", 
"Iron Hammer": "made with 10 iron bar and 3 wood",
"Torch": "A torch can be crafted with one gel and one wood",
"Wood": "Wood is found from chopping down trees with an axe",
"Iron Axe": "made with 9 iron bar and 3 wood",
"Iron Ore": "Iron ore is found underground and in caverns",
"Copper Ore": "Copper ore is found on the surface, underground and in caverns",
"Gold Ore": "Gold ore is found underground and in caverns, it is less common than iron, silver and copper",
"Silver Ore": "Silver ore is found underground and in caverns, it is less common than iron and copper",
"Copper Watch": "made with 10 copper bar and 1 chain",
"Silver Watch": "made with 10 silver bar and 1 chain",
"Gold Watch": "made with 10 gold bar and 1 chain",
"Depth Meter": "made with 10 copper bars, 8 silver bars and 6 gold bars",
"Gold Bar": "A gold bar can be made using the furnace to smelt three gold ore",
"Copper Bar": "A copper bar can be made using the furnace to smelt three copper ore",
"Silver Bar": "4 silver ore smelts to be a silver bar",
"Iron Bar": "An iron bar can be made using the furnace to smelt three iron ore.",
"Gel": "Gel is found from defeating slime enemies",
"Wooden Sword": "made with 7 wood",
"Wooden Door": "a wooden door is made with 6 wood while standing by a crafting table",
"Stone Wall": "4 stone wall is made from 1 stone block",
"Acorn": "Acorns are found from chopping down trees",
"Lesser Healing Potion": "dropped from enemies, found in chests or made with 1 mushroom, 2 gel and 2 bottles",
"Life Crystal": "a life crystal can be found in underground caverns",
"Dirt Wall": "4 dirt wall is made from 1 dirt block",
"Bottle": "A bottle can be made by using 1 glass block at a furnace",
"Wooden Table": "a wooden table is made with 8 wood while standing by a crafting table",
"Furnace": "A furnace can be crafted by using twenty stone blocks, four wood, and three torches",
"Wooden Chair": "a wooden chair is made with 4 wood while standing by a crafting table",
"Iron Anvil": "An iron anvil requires five iron bars and you need to stand near a work bench.",
"Work Bench": "A work bench can be made with ten wood",
"Goggles": "made with 2 lens",
"Lens": "dropped from defeating suspicious looking eyes",
"Wooden Bow": "made with 10 wood",
"Wooden Arrow": "made with any wood and stone block",
"Flaming Arrow": "made with 10 wooden arrow and 1 torch",
"Shuriken": "Found in chests",
"Suspicious Looking Eye": "Can be found in chests or crafted with 10 lens",
"Demon Bow": "made with 8 demonite bars",
"War Axe of the Night": "made with 10 demonite bars",
"Light's Bane": "made with 10 demonite bars",
"Unholy Arrow": "made with 5 wooden arrows and 1 worm tooth",
"Chest": "a chest is made with 8 wood and 2 iron bars while near a crafting table",
"Band of Regeneration": "can be found in chests",
"Magic Mirror": "can be found in chests",
"Jester's Arrow": "made with 20 wooden arrows and 1 fallen star",
"Angel Statue": "a statue is made with 100 stone blocks",
"Cloud in a Bottle": "can be found in chests",
"Hermes Boots": "can be found in chests",
"Enchanted Boomerang": "can be found in gold chests",
"Demonite Ore": "demonite ore can be found in the corruption areas and mined with a gold pickaxe or better. Defeating bosses also dropes the ore.",
"Demonite Bar": "A demonite bar can be made using the furnace to smelt three demonite ore.",
"Heart": "found from defeating enemies, or dropped by a heart statue",
"Corrupt Seeds": "They drop from the Eye of Cthulhu and can be purchased from the Dryad for 5 Silver each during a Blood Moon in a Corrupt world.",
"Vile Mushroom": "A Vile Mushroom is found on grass in the Corruption, where they can be cut with a single swing.",
"Ebonstone Block": "can be mined in the corruption biome",
"Grass Seeds": "purchased from the Dryad for 20 Copper each",
"Sunflower": "Flowers that grow on the surface",
"Vilethorn": "it is one of the possible drops from destroying a Shadow Orb in the Corruption, it can also be obtained from Corrupt Crates",
"Starfury": "Can be found in Sky chests",
"Purification Powder": "can be purchased for 75 copper from the dryad",
"Vile Powder": "can be purchased or can be crafted from 1 vile mushroom, needs an alchemy table",
"Rotten Chunk": "drop from defeating Eaters of Souls, Devourers, or Corruptors.",
"Worm Tooth": "dropped by Devourers in The Corruption.",
"Worm Food": "crafted with 30 vile powder and 15 rotten chunks near a demon or crimson alter.",
"Copper Coin": "a Copper coin is found by defeating enemies",
"Silver Coin": "a silver coin is made from 100 copper coins, or picked up from enemies",
"Gold Coin": "a gold coin is made from 100 silver coins, or picked up from enemies",
"Platinum Coin": "A platinum coin is made from 100 gold coins, or picked up from enemies",
"Fallen Star": "fallen stars randomly fall from the sky at night.",
"Copper Greaves": "made with 20 copper bar",
"Iron Greaves": "made with 25 iron bar",
"Silver Greaves": "made with 25 silver bar",
"Gold Greaves": "made with 30 gold bars",
"Copper Chainmail": "made with 25 copper bar",
"Iron Chainmail": "made with 30 iron bar",
"Silver Chainmail": "made with 30 silver bar",
"Gold Chainmail": "made with 35 gold bar",
"Grappling Hook": "Made with 3 chain and one hook",
"Chain": "made with any iron bar",
"Shadow Scale": "a common drop from the Eater of Worlds",
"Piggy Bank": "Purchased from the merchant",
"Mining Helmet": "can be purchased from the Merchant",
"Copper Helmet": "made with 15 copper bar",
"Iron Helmet": "made with 20 iron bar",
"Silver Helmet": "made with 20 silver bar",
"Gold Helmet": "made with 25 gold bar",
"Wood Wall": "made from 1 wood",
"Wood Platform": "made from 1 wood",
"Flintlock Pistol": "can be bought from the Arms Dealer.",
"Musket": "always drops from the first Shadow Orb destroyed in a Corruption world",
"Musket Ball": "can be bought from the Arms Dealer",
"Minishark": "can be bought from the Arms Dealer",
"Iron Bow": "an iron bow is made with 7 iron bars",
"Shadow Greaves": "a shadow greaves are made with 20 demonite bar and 15 shadow scales.",
"Shadow Scalemail": "a shadow scalemail is made with 25 demonite bar and 20 shadow scale.",
"Shadow Helmet": "a shadow helmet is made with 15 demonite bar and 10 shadow scale.",
"Nightmare Pickaxe" : "is made with 12 demonite bar and 6 shadow scale.",
"The Breaker" : "is made with 10 demonite bar and 5 shadow scale.",
"Candle": "a candle is made with 1 gold bar and 1 torch",
"Copper Chandelier": "is made with 4 copper bar, 4 torches, and 1 chain",
"Silver Chandelier": "is made with 4 silver bar, 4 torches, and 1 chain",
"Gold Chandelier": "is made with 4 gold bar, 4 torches, and 1 chain",
"Mana Crystal": "a mana crystal is made using three fallen stars.",
"Lesser Mana Potion": "",
"Band of Starpower
"Flower of Fire
"Magic Missile
"Dirt Rod
"Meteorite" "meteorite ore can be found at a Meteorite crash site. A Meteorite crash site has \
    a 50% chance of spawning the next midnight after a Shadow Orb or Crimson Heart is smashed.",
"Meteorite Bar": "A meteorite bar can be made using the furnace to smelt three meteorite ore.",
"Hook (crafting material)
"Flamarang
"Molten Fury
"Fiery Greatsword
"Molten Pickaxe
"Meteor Helmet": "a meteor helmet is made with 25 meteorite bars",
"Meteor Suit": "a meteor suit is made with 35 meteorite bars",
"Meteor Leggings": "meteor leggings are made with 30 meteorite bars",
"Bottled Water
"Space Gun
"Rocket Boots
"Gray Brick": "gray brick can be made by using 2 stone at a furnace.",
"Gray Brick Wall
"Red Brick": "red brick can be made by using 2 clay at a furnace.",
"Red Brick Wall
"Clay Block": "clay is found most commonly at the surface and is a slightly darker color than dirt.",
"Blue Brick
"Blue Brick Wall": "made from blue brick",
"Chain Lantern": "",
"Green Brick": "",
"Green Brick Wall": "made from green brick",
"Pink Brick": "",
"Pink Brick Wall": "made from pink brick".
"Gold Brick": "",
"Gold Brick Wall": "made from gold brick",
"Silver Brick": "",
"Silver Brick Wall": "made from silver brick",
"Copper Brick": "",
"Copper Brick Wall": "made from copper brick",
"Spike"
"Water Candle": "Found inside the dungeon",
"Book": "",
"Cobweb": "Found in the spider biome or underground.",
"Necro Helmet
"Necro Breastplate
"Necro Greaves
"Bone
"Muramasa
"Cobalt Shield
"Aqua Scepter
"Lucky Horseshoe
"Shiny Red Balloon
"Harpoon
"Spiky Ball
"Ball O' Hurt
"Blue Moon
"Handgun
"Water Bolt
"Bomb
"Dynamite
"Grenade
"Sand Block": "Sand can be found in the desert biome or at the beach on the far left or right of the map.",
"Glass
"Sign": "a sign is crafted with with 6 wood while standing by a crafting table",
"Ash Block
"Obsidian
"Hellstone
"Hellstone Bar
"Mud Block
"Sapphire
"Ruby
"Emerald
"Topaz
"Amethyst
"Diamond
"Glowing Mushroom
"Star
"Ivy Whip
"Breathing Reed
"Flipper
"Healing Potion
"Mana Potion
"Blade of Grass
"Thorn Chakram
"Obsidian Brick
"Obsidian Skull
"Mushroom Grass Seeds
"Jungle Grass Seeds
"Wooden Hammer
"Star Cannon
"Blue Phaseblade
"Red Phaseblade
"Green Phaseblade
"Purple Phaseblade
"White Phaseblade
"Yellow Phaseblade
"Meteor Hamaxe
"Empty Bucket
"Water Bucket
"Lava Bucket
"Jungle Rose
"Stinger
"Vine
"Feral Claws
"Anklet of the Wind
"Staff of Regrowth
"Hellstone Brick
"Whoopie Cushion
"Shackle
"Molten Hamaxe
"Flamelash
"Phoenix Blaster
"Sunfury
"Hellforge
"Clay Pot
"Nature's Gift
"Bed
"Silk
"Lesser Restoration Potion
"Restoration Potion
"Jungle Hat": "a jungle hat requires 8 jungle spores",
"Jungle Shirt": "a jungle shirt requires 16 jungle spores, and 10 stingers",
"Jungle Pants": "jungle pants are made with 8 jungle spores and 2 vines",
"Molten Helmet": "a molten helmet is made with 30 hellstone bars",
"Molten Breastplate": "a molten breastplate is made with 40 hellstone bars",
"Molten Greaves": "molten greaves is made with 35 hellstone bars",
"Meteor Shot
"Sticky Bomb": "sticky bomb is made with a bomb and gel",
"Black Lens
"Sunglasses
"Wizard Hat
"Top Hat
"Tuxedo Shirt
"Tuxedo Pants
"Summer Hat
"Bunny Hood
"Plumber's Hat
"Plumber's Shirt
"Plumber's Pants
"Hero's Hat
"Hero's Shirt
"Hero's Pants
"Fish Bowl":"a fish bowl is made with 2 goldfish and 1 bottled water",
"Archaeologist's Hat
"Archaeologist's Jacket
"Archaeologist's Pants
"Black Thread
"Green Thread
"Ninja Hood
"Ninja Shirt
"Ninja Pants
"Leather
"Red Hat
"Goldfish": "Goldfish can be found in pools of water or found when it's raining",
"Robe
"Robot Hat
"Gold Crown
"Hellfire Arrow": "made with 100 wooden arrows and 1 hellstone bar",
"Sandgun
"Guide Voodoo Doll
"Diving Helmet
"Familiar Shirt
"Familiar Pants
"Familiar Wig
"Demon Scythe
"Night's Edge
"Dark Lance
"Coral
"Cactus
"Trident
"Silver Bullet
"Throwing Knife
"Spear
"Blowpipe
"Glowstick
"Seed
"Wooden Boomerang
"Aglet
"Sticky Glowstick": "sticky glowsticks are made with gel and a glowstick",
"Poisoned Knife
"Obsidian Skin Potion
"Regeneration Potion
"Swiftness Potion
"Gills Potion
"Ironskin Potion
"Mana Regeneration Potion
"Magic Power Potion
"Featherfall Potion
"Spelunker Potion
"Invisibility Potion
"Shine Potion
"Night Owl Potion
"Battle Potion
"Thorns Potion
"Water Walking Potion
"Archery Potion
"Hunter Potion
"Gravitation Potion
"Gold Chest
"Daybloom Seeds
"Moonglow Seeds
"Blinkroot Seeds
"Deathweed Seeds
"Waterleaf Seeds
"Fireblossom Seeds
"Daybloom
"Moonglow
"Blinkroot
"Deathweed
"Waterleaf
"Fireblossom
"Shark Fin
"Feather
"Tombstone
"Mime Mask
"Antlion Mandible
"Illegal Gun Parts
"The Doctor's Shirt
"The Doctor's Pants
"Golden Key
"Shadow Chest
"Shadow Key
"Obsidian Brick Wall
"Jungle Spores
"Loom
"Piano
"Dresser
"Bench
"Bathtub
"Red Banner
"Green Banner
"Blue Banner
"Yellow Banner
"Lamp Post
"Tiki Torch": "a tiki torch is made with 3 wood and 1 torch",
"Barrel
"Chinese Lantern
"Cooking Pot
"Safe
"Skull Lantern
"Trash Can
"Candelabra
"Pink Vase
"Mug
"Keg
"Ale
"Bookcase
"Throne
"Bowl
"Bowl of Soup
"Toilet
"Grandfather Clock
"Armor Statue
"Goblin Battle Standard
"Tattered Cloth
"Sawmill": "a sawmill is crafted with 10 wood, 2 iron bars and 1 iron chain",
"Cobalt Ore
"Mythril Ore
"Adamantite Ore
"Pwnhammer
"Excalibur
"Hallowed Seeds
"Ebonsand Block
"Cobalt Hat
"Cobalt Helmet
"Cobalt Mask
"Cobalt Breastplate
"Cobalt Leggings
"Mythril Hood
"Mythril Helmet
"Mythril Hat
"Mythril Chainmail
"Mythril Greaves
"Cobalt Bar" : "a cobalt bar is made by smelting three cobalt ore at a furnace.",
"Mythril Bar
"Cobalt Chainsaw
"Mythril Chainsaw
"Cobalt Drill
"Mythril Drill
"Adamantite Chainsaw
"Adamantite Drill
"Dao of Pow
"Mythril Halberd
"Adamantite Bar
"Glass Wall
"Compass
"Diving Gear
"GPS
"Obsidian Horseshoe
"Obsidian Shield
"Tinkerer's Workshop
"Cloud in a Balloon
"Adamantite Headgear
"Adamantite Helmet
"Adamantite Mask
"Adamantite Breastplate
"Adamantite Leggings
"Spectre Boots
"Adamantite Glaive
"Toolbelt
"Pearlsand Block
"Pearlstone Block
"Mining Shirt
"Mining Pants
"Pearlstone Brick
"Iridescent Brick
"Mudstone Brick
"Cobalt Brick
"Mythril Brick
"Pearlstone Brick Wall
"Iridescent Brick Wall
"Mudstone Brick Wall
"Cobalt Brick Wall
"Mythril Brick Wall
"Holy Water": "holy water requires 5 pixie dust, 1 bottled water and 1 hallowed seeds",
"Unholy Water": "unholy water requires 1 bottled water, 1 corrupt seeds and 1 ebonsand block",
"Silt Block
"Fairy Bell
"Breaker Blade
"Blue Torch": "blue torches are made with 3 torches and 1 sapphire",
"Red Torch": "red torches are made with 3 torches and 1 ruby",
"Green Torch": "green torches are made with 3 torches and 1 emerald",
"Purple Torch:" "purple torches are made with 3 torches and 1 amethyst",
"White Torch": "white torches are made with 3 torches and 1 diamond",
"Yellow Torch
"Demon Torch
"Clockwork Assault Rifle
"Cobalt Repeater
"Mythril Repeater
"Dual Hook
"Star Statue
"Sword Statue
"Slime Statue
"Goblin Statue
"Shield Statue
"Bat Statue
"Fish Statue
"Bunny Statue
"Skeleton Statue
"Reaper Statue
"Woman Statue
"Imp Statue
"Gargoyle Statue
"Gloom Statue
"Hornet Statue
"Bomb Statue
"Crab Statue
"Hammer Statue
"Potion Statue
"Spear Statue
"Cross Statue
"Jellyfish Statue
"Bow Statue
"Boomerang Statue
"Boot Statue
"Chest Statue
"Bird Statue
"Axe Statue
"Corrupt Statue
"Tree Statue
"Anvil Statue
"Pickaxe Statue
"Mushroom Statue
"Eyeball Statue
"Pillar Statue
"Heart Statue
"Pot Statue
"Sunflower Statue
"King Statue
"Queen Statue
"Piranha Statue
"Planked Wall
"Wooden Beam
"Adamantite Repeater
"Adamantite Sword
"Cobalt Sword
"Mythril Sword
"Moon Charm
"Ruler
"Crystal Ball
"Disco Ball
"Sorcerer Emblem
"Warrior Emblem
"Ranger Emblem
"Demon Wings
"Angel Wings
"Magical Harp
"Rainbow Rod
"Ice Rod
"Neptune's Shell
"Mannequin
"Greater Healing Potion
"Greater Mana Potion
"Pixie Dust
"Crystal Shard
"Clown Hat
"Clown Shirt
"Clown Pants
"Flamethrower
"Bell
"Harp
"Red Wrench
"Wire Cutter
"Active Stone Block
"Inactive Stone Block
"Lever
"Laser Rifle
"Crystal Bullet
"Holy Arrow": "made with 200 wooden arrow, 3 pixie dust and 1 unicorn horn",
"Magic Dagger
"Crystal Storm
"Cursed Flames
"Soul of Light
"Soul of Night
"Cursed Flame
"Cursed Torch": "cursed torches are made with 33 torches and 1 cursed flame",
"Adamantite Forge
"Mythril Anvil
"Unicorn Horn
"Dark Shard
"Light Shard
"Red Pressure Plate
"Wire
"Spell Tome
"Star Cloak
"Megashark
"Shotgun
"Philosopher's Stone
"Titan Glove
"Cobalt Naginata
"Switch
"Dart Trap
"Boulder
"Green Pressure Plate
"Gray Pressure Plate
"Brown Pressure Plate
"Mechanical Eye
"Cursed Arrow": "made with 150 wooden arrow and 1 cursed flame",
"Cursed Bullet
"Soul of Fright": "soul of fright is dropped by defeating skeletron prime",
"Soul of Might": "soul of might is dropped by defeating destoryer of worlds",
"Soul of Sight": "soul of sight is dropped by defeating the twins"
"Gungnir
"Hallowed Plate Mail
"Hallowed Greaves
"Hallowed Helmet
"Cross Necklace
"Mana Flower
"Mechanical Worm
"Mechanical Skull
"Hallowed Headgear
"Hallowed Mask
"Slime Crown
"Light Disc
"Music Box (Overworld Day)
"Music Box (Eerie)
"Music Box (Night)
"Music Box (Title)
"Music Box (Underground)
"Music Box (Boss 1)
"Music Box (Jungle)
"Music Box (Corruption)
"Music Box (Underground Corruption)
"Music Box (The Hallow)
"Music Box (Boss 2)
"Music Box (Underground Hallow)
"Music Box (Boss 3)
"Soul of Flight
"Music Box
"Demonite Brick
"Hallowed Repeater
"Drax
"Explosives
"Inlet Pump
"Outlet Pump
"1 Second Timer
"3 Second Timer
"5 Second Timer
"Candy Cane Block
"Candy Cane Wall
"Santa Hat
"Santa Shirt
"Santa Pants
"Green Candy Cane Block
"Green Candy Cane Wall
"Snow Block
"Snow Brick
"Snow Brick Wall
"Blue Light
"Red Light
"Green Light
"Blue Present
"Green Present
"Yellow Present
"Snow Globe
"Carrot
"Adamantite Beam
"Adamantite Beam Wall
"Demonite Brick Wall
"Sandstone Brick
"Sandstone Brick Wall
"Ebonstone Brick
"Ebonstone Brick Wall
"Red Stucco
"Yellow Stucco
"Green Stucco
"Gray Stucco
"Red Stucco Wall
"Yellow Stucco Wall
"Green Stucco Wall
"Gray Stucco Wall
"Ebonwood
"Rich Mahogany
"Pearlwood
"Ebonwood Wall
"Rich Mahogany Wall
"Pearlwood Wall
"Ebonwood Chest
"Rich Mahogany Chest
"Pearlwood Chest
"Ebonwood Chair
"Rich Mahogany Chair
"Pearlwood Chair
"Ebonwood Platform
"Rich Mahogany Platform
"Pearlwood Platform
"Bone Platform
"Ebonwood Work Bench
"Rich Mahogany Work Bench
"Pearlwood Work Bench
"Ebonwood Table
"Rich Mahogany Table
"Pearlwood Table
"Ebonwood Piano
"Rich Mahogany Piano
"Pearlwood Piano
"Ebonwood Bed
"Rich Mahogany Bed
"Pearlwood Bed
"Ebonwood Dresser
"Rich Mahogany Dresser
"Pearlwood Dresser
"Ebonwood Door
"Rich Mahogany Door
"Pearlwood Door
"Ebonwood Sword
"Ebonwood Hammer
"Ebonwood Bow
"Rich Mahogany Sword
"Rich Mahogany Hammer
"Rich Mahogany Bow
"Pearlwood Sword
"Pearlwood Hammer
"Pearlwood Bow
"Rainbow Brick
"Rainbow Brick Wall
"Ice Block
"Red's Wings
"Red's Helmet
"Red's Breastplate
"Red's Leggings
"Fish
"Ice Boomerang
"Keybrand
"Cutlass
"Boreal Wood Work Bench
"True Excalibur
"True Night's Edge
"Frostbrand
"Boreal Wood Table
"Red Potion
"Tactical Shotgun
"Ivy Chest
"Ice Chest
"Marrow
"Unholy Trident
"Frost Helmet
"Frost Breastplate
"Frost Leggings
"Tin Helmet
"Tin Chainmail
"Tin Greaves
"Lead Helmet
"Lead Chainmail
"Lead Greaves
"Tungsten Helmet
"Tungsten Chainmail
"Tungsten Greaves
"Platinum Helmet
"Platinum Chainmail
"Platinum Greaves
"Tin Ore": "tin ore can be found on or near the surface, in the cavern biome or underground and can be mined with any pickaxe.",
"Lead Ore
"Tungsten Ore
"Platinum Ore": "platinum ore can be found underground",
"Tin Bar": "A tin bar can be made using the furnace to smelt three tin ore",
"Lead Bar
"Tungsten Bar
"Platinum Bar": "A platinum bar can be made using the furnace to smelt four platinum ore.",
"Tin Watch
"Tungsten Watch
"Platinum Watch
"Tin Chandelier
"Tungsten Chandelier
"Platinum Chandelier
"Platinum Candle
"Platinum Candelabra
"Platinum Crown
"Lead Anvil
"Tin Brick
"Tungsten Brick
"Platinum Brick
"Tin Brick Wall
"Tungsten Brick Wall
"Platinum Brick Wall
"Beam Sword
"Ice Blade
"Ice Bow
"Frost Staff
"Wood Helmet
"Wood Breastplate
"Wood Greaves
"Ebonwood Helmet
"Ebonwood Breastplate
"Ebonwood Greaves
"Rich Mahogany Helmet
"Rich Mahogany Breastplate
"Rich Mahogany Greaves
"Pearlwood Helmet
"Pearlwood Breastplate
"Pearlwood Greaves
"Amethyst Staff
"Topaz Staff
"Sapphire Staff
"Emerald Staff
"Ruby Staff
"Diamond Staff
"Grass Wall
"Jungle Wall
"Flower Wall
"Jetpack
"Butterfly Wings
"Cactus Wall
"Cloud
"Cloud Wall
"Seaweed
"Rune Hat
"Rune Robe
"Mushroom Spear
"Terra Blade
"Grenade Launcher
"Rocket Launcher
"Proximity Mine Launcher
"Fairy Wings
"Slime Block
"Flesh Block
"Mushroom Wall
"Rain Cloud
"Bone Block
"Frozen Slime Block
"Bone Block Wall
"Slime Block Wall
"Flesh Block Wall
"Rocket I
"Rocket II
"Rocket III
"Rocket IV
"Asphalt Block
"Cobalt Pickaxe
"Mythril Pickaxe
"Adamantite Pickaxe
"Clentaminator
"Green Solution
"Blue Solution
"Purple Solution
"Dark Blue Solution
"Red Solution
"Harpy Wings
"Bone Wings
"Hammush
"Nettle Burst
"Ankh Banner
"Snake Banner
"Omega Banner
"Crimson Helmet
"Crimson Scalemail
"Crimson Greaves
"Blood Butcherer
"Tendon Bow
"Flesh Grinder
"Deathbringer Pickaxe
"Blood Lust Cluster
"The Undertaker
"The Meatball
"The Rotted Fork
"Eskimo Hood
"Eskimo Coat
"Eskimo Pants
"Living Wood Chair
"Cactus Chair
"Bone Chair
"Flesh Chair
"Mushroom Chair
"Bone Work Bench
"Cactus Work Bench
"Flesh Work Bench
"Mushroom Work Bench
"Slime Work Bench
"Cactus Door
"Flesh Door
"Mushroom Door
"Living Wood Door
"Bone Door
"Flame Wings
"Frozen Wings
"Spectre Wings
"Sunplate Block
"Disc Wall
"Skyware Chair
"Bone Table
"Flesh Table
"Living Wood Table
"Skyware Table
"Living Wood Chest
"Living Wood Wand
"Purple Ice Block
"Pink Ice Block
"Red Ice Block
"Crimstone Block
"Skyware Door
"Skyware Chest
"Steampunk Hat
"Steampunk Shirt
"Steampunk Pants
"Bee Hat
"Bee Shirt
"Bee Pants
"World Banner
"Sun Banner
"Gravity Banner
"Pharaoh's Mask
"Actuator
"Blue Wrench
"Green Wrench
"Blue Pressure Plate
"Yellow Pressure Plate
"Discount Card
"Lucky Coin
"Unicorn on a Stick
"Sandstorm in a Bottle
"Boreal Wood Sofa
"Beach Ball
"Charm of Myths
"Moon Shell
"Star Veil
"Water Walking Boots
"Tiara
"Pharaoh's Robe
"Green Cap
"Mushroom Cap
"Tam O' Shanter
"Mummy Mask
"Mummy Shirt
"Mummy Pants
"Cowboy Hat
"Cowboy Jacket
"Cowboy Pants
"Pirate Hat
"Pirate Shirt
"Pirate Pants
"Viking Helmet
"Crimtane Ore
"Cactus Sword
"Cactus Pickaxe
"Ice Brick
"Ice Brick Wall
"Adhesive Bandage
"Armor Polish
"Bezoar
"Blindfold
"Fast Clock
"Megaphone
"Nazar
"Vitamins
"Trifold Map
"Cactus Helmet
"Cactus Breastplate
"Cactus Leggings
"Power Glove
"Lightning Boots
"Sun Stone
"Moon Stone
"Armor Bracing
"Medicated Bandage
"The Plan
"Countercurse Mantra
"Coin Gun
"Lava Charm
"Obsidian Water Walking Boots
"Lava Waders
"Pure Water Fountain
"Desert Water Fountain
"Shadewood
"Shadewood Door
"Shadewood Platform
"Shadewood Chest
"Shadewood Chair
"Shadewood Work Bench
"Shadewood Table
"Shadewood Dresser
"Shadewood Piano
"Shadewood Bed
"Shadewood Sword
"Shadewood Hammer
"Shadewood Bow
"Shadewood Helmet
"Shadewood Breastplate
"Shadewood Greaves
"Shadewood Wall
"Cannon
"Cannonball
"Flare Gun
"Flare
"Bone Wand
"Leaf Wand
"Flying Carpet
"Avenger Emblem
"Mechanical Glove
"Land Mine
"Paladin's Shield
"Web Slinger
"Jungle Water Fountain
"Icy Water Fountain
"Corrupt Water Fountain
"Crimson Water Fountain
"Hallowed Water Fountain
"Blood Water Fountain
"Umbrella
"Chlorophyte Ore
"Steampunk Wings
"Snowball
"Ice Skates
"Snowball Launcher
"Web Covered Chest
"Climbing Claws
"Ancient Iron Helmet
"Ancient Gold Helmet
"Ancient Shadow Helmet
"Ancient Shadow Scalemail
"Ancient Shadow Greaves
"Ancient Necro Helmet
"Ancient Cobalt Helmet
"Ancient Cobalt Breastplate
"Ancient Cobalt Leggings
"Black Belt
"Boomstick
"Rope
"Campfire
"Marshmallow
"Marshmallow on a Stick
"Cooked Marshmallow
"Red Rocket
"Green Rocket
"Blue Rocket
"Yellow Rocket
"Ice Torch
"Shoe Spikes
"Tiger Climbing Gear
"Tabi
"Pink Eskimo Hood
"Pink Eskimo Coat
"Pink Eskimo Pants
"Pink Thread
"Mana Regeneration Band
"Sandstorm in a Balloon
"Master Ninja Gear
"Rope Coil": "rope coil is made with 10 rope",
"Blowgun
"Blizzard in a Bottle
"Frostburn Arrow": "made with 10 wooden arrows and 1 ice torch",
"Pickaxe Axe
"Cobalt Waraxe
"Mythril Waraxe
"Adamantite Waraxe
"Eater's Bone
"Blend-O-Matic
"Meat Grinder
"Extractinator
"Solidifier
"Amber
"Confetti Gun
"Chlorophyte Mask
"Chlorophyte Helmet
"Chlorophyte Headgear
"Chlorophyte Plate Mail
"Chlorophyte Greaves
"Chlorophyte Bar
"Red Dye
"Orange Dye
"Yellow Dye
"Lime Dye
"Green Dye
"Teal Dye
"Cyan Dye
"Sky Blue Dye
"Blue Dye
"Purple Dye
"Violet Dye
"Pink Dye
"Red and Black Dye
"Orange and Black Dye
"Yellow and Black Dye
"Lime and Black Dye
"Green and Black Dye
"Teal and Black Dye
"Cyan and Black Dye
"Sky Blue and Black Dye
"Blue and Black Dye
"Purple and Black Dye
"Violet and Black Dye
"Pink and Black Dye
"Flame Dye
"Flame and Black Dye
"Green Flame Dye
"Green Flame and Black Dye
"Blue Flame Dye
"Blue Flame and Black Dye
"Silver Dye
"Bright Red Dye
"Bright Orange Dye
"Bright Yellow Dye
"Bright Lime Dye
"Bright Green Dye
"Bright Teal Dye
"Bright Cyan Dye
"Bright Sky Blue Dye
"Bright Blue Dye
"Bright Purple Dye
"Bright Violet Dye
"Bright Pink Dye
"Black Dye
"Red and Silver Dye
"Orange and Silver Dye
"Yellow and Silver Dye
"Lime and Silver Dye
"Green and Silver Dye
"Teal and Silver Dye
"Cyan and Silver Dye
"Sky Blue and Silver Dye
"Blue and Silver Dye
"Purple and Silver Dye
"Violet and Silver Dye
"Pink and Silver Dye
"Intense Flame Dye
"Intense Green Flame Dye
"Intense Blue Flame Dye
"Rainbow Dye
"Intense Rainbow Dye
"Yellow Gradient Dye
"Cyan Gradient Dye
"Violet Gradient Dye
"Paintbrush
"Paint Roller
"Red Paint
"Orange Paint
"Yellow Paint
"Lime Paint
"Green Paint
"Teal Paint
"Cyan Paint
"Sky Blue Paint
"Blue Paint
"Purple Paint
"Violet Paint
"Pink Paint
"Deep Red Paint
"Deep Orange Paint
"Deep Yellow Paint
"Deep Lime Paint
"Deep Green Paint
"Deep Teal Paint
"Deep Cyan Paint
"Deep Sky Blue Paint
"Deep Blue Paint
"Deep Purple Paint
"Deep Violet Paint
"Deep Pink Paint
"Black Paint
"White Paint
"Gray Paint
"Paint Scraper
"Lihzahrd Brick
"Lihzahrd Brick Wall
"Slush Block
"Palladium Ore
"Orichalcum Ore
"Titanium Ore
"Teal Mushroom
"Green Mushroom
"Sky Blue Flower
"Yellow Marigold
"Blue Berries
"Lime Kelp
"Pink Prickly Pear
"Orange Bloodroot
"Red Husk
"Cyan Husk
"Violet Husk
"Purple Mucos
"Black Ink
"Dye Vat
"Bee Gun
"Possessed Hatchet
"Bee Keeper
"Hive
"Honey Block
"Hive Wall
"Crispy Honey Block
"Honey Bucket
"Hive Wand
"Beenade
"Gravity Globe
"Honey Comb
"Abeemination
"Bottled Honey
"Rain Hat
"Rain Coat
"Lihzahrd Door
"Dungeon Door
"Lead Door
"Iron Door
"Temple Key
"Lihzahrd Chest
"Lihzahrd Chair
"Lihzahrd Table
"Lihzahrd Work Bench
"Super Dart Trap
"Flame Trap
"Spiky Ball Trap
"Spear Trap
"Wooden Spike
"Lihzahrd Pressure Plate
"Lihzahrd Statue
"Lihzahrd Watcher Statue
"Lihzahrd Guardian Statue
"Wasp Gun
"Piranha Gun
"Pygmy Staff
"Pygmy Necklace
"Tiki Mask
"Tiki Shirt
"Tiki Pants
"Leaf Wings
"Blizzard in a Balloon
"Bundle of Balloons
Bat Wings
Bone Sword
Hercules Beetle
Smoke Bomb
Bone Key
Nectar
Tiki Totem
Lizard Egg
Grave Marker
Cross Grave Marker
Headstone
Gravestone
Obelisk
Leaf Blower
Chlorophyte Bullet
Parrot Cracker
Strange Glowing Mushroom
Seedling
Wisp in a Bottle
Palladium Bar
Palladium Sword
Palladium Pike
Palladium Repeater
Palladium Pickaxe
Palladium Drill
Palladium Chainsaw
Orichalcum Bar
Orichalcum Sword
Orichalcum Halberd
Orichalcum Repeater
Orichalcum Pickaxe
Orichalcum Drill
Orichalcum Chainsaw
Titanium Bar
Titanium Sword
Titanium Trident
Titanium Repeater
Titanium Pickaxe
Titanium Drill
Titanium Chainsaw
Palladium Mask
Palladium Helmet
Palladium Headgear
Palladium Breastplate
Palladium Leggings
Orichalcum Mask
Orichalcum Helmet
Orichalcum Headgear
Orichalcum Breastplate
Orichalcum Leggings
Titanium Mask
Titanium Helmet
Titanium Headgear
Titanium Breastplate
Titanium Leggings
Orichalcum Anvil
Titanium Forge
Palladium Waraxe
Orichalcum Waraxe
Titanium Waraxe
Hallowed Bar
Chlorophyte Claymore
Chlorophyte Saber
Chlorophyte Partisan
Chlorophyte Shotbow
Chlorophyte Pickaxe
Chlorophyte Drill
Chlorophyte Chainsaw
Chlorophyte Greataxe
Chlorophyte Warhammer
Chlorophyte Arrow
Amethyst Hook
Topaz Hook
Sapphire Hook
Emerald Hook
Ruby Hook
Diamond Hook
Amber Mosquito
Umbrella Hat
Nimbus Rod
Orange Torch
Crimsand Block
Bee Cloak
Eye of the Golem
Honey Balloon
Blue Horseshoe Balloon
White Horseshoe Balloon
Yellow Horseshoe Balloon
Frozen Turtle Shell
Sniper Rifle
Venus Magnum
Crimson Rod
Crimtane Bar
Stynger
Flower Pow
Rainbow Gun
Stynger Bolt
Chlorophyte Jackhammer
Teleporter
Flower of Frost
Uzi
Magnet Sphere
Purple Stained Glass
Yellow Stained Glass
Blue Stained Glass
Green Stained Glass
Red Stained Glass
Multicolored Stained Glass
Skeletron Hand
Skull
Balla Hat
Gangsta Hat
Sailor Hat
Eye Patch
Sailor Shirt
Sailor Pants
Skeletron Mask
Amethyst Robe
Topaz Robe
Sapphire Robe
Emerald Robe
Ruby Robe
Diamond Robe
White Tuxedo Shirt
White Tuxedo Pants
Panic Necklace
Life Fruit
Lihzahrd Altar
Lihzahrd Power Cell
Picksaw
Heat Ray
Staff of Earth
Golem Fist
Water Chest
Binoculars
Rifle Scope
Destroyer Emblem
High Velocity Bullet
Jellyfish Necklace
Zombie Arm
The Axe
Ice Sickle
Clothier Voodoo Doll
Poison Staff
Slime Staff
Poison Dart
Eye Spring
Toy Sled
Book of Skulls
KO Cannon
Pirate Map
Turtle Helmet
Turtle Scale Mail
Turtle Leggings
Snowball Cannon
Bone Pickaxe
Magic Quiver
Magma Stone
Obsidian Rose
Bananarang
Chain Knife
Rod of Discord
Death Sickle
Turtle Shell
Tissue Sample
Vertebrae
Bloody Spine
Ichor
Ichor Torch
"Ichor Arrow": "made with 150 wooden arrows and 1 ichor",
Ichor Bullet
Golden Shower
Bunny Cannon
Explosive Bunny
Vial of Venom
Flask of Venom
"Venom Arrow": "made with 35 wooden arrow and 1 vial of venom",
Venom Bullet
Fire Gauntlet
Cog
Confetti
Nanites
Explosive Powder
Gold Dust
Party Bullet
Nano Bullet
Exploding Bullet
Golden Bullet
Flask of Cursed Flames
Flask of Fire
Flask of Gold
Flask of Ichor
Flask of Nanites
Flask of Party
Flask of Poison
Eye of Cthulhu Trophy
Eater of Worlds Trophy
Brain of Cthulhu Trophy
Skeletron Trophy
Queen Bee Trophy
Wall of Flesh Trophy
Destroyer Trophy
Skeletron Prime Trophy
Retinazer Trophy
Spazmatism Trophy
Plantera Trophy
Golem Trophy
Blood Moon Rising
The Hanged Man
Glory of the Fire
Bone Warp
Wall Skeleton
Hanging Skeleton
Blue Slab Wall
Blue Tiled Wall
Pink Slab Wall
Pink Tiled Wall
Green Slab Wall
Green Tiled Wall
Blue Brick Platform
Pink Brick Platform
Green Brick Platform
Metal Shelf
Brass Shelf
Wood Shelf
Brass Lantern
Caged Lantern
Carriage Lantern
Alchemy Lantern
Diabolist Lamp
Oil Rag Sconse
Blue Dungeon Chair
Blue Dungeon Table
Blue Dungeon Work Bench
Green Dungeon Chair
Green Dungeon Table
Green Dungeon Work Bench
Pink Dungeon Chair
Pink Dungeon Table
Pink Dungeon Work Bench
Blue Dungeon Candle
Green Dungeon Candle
Pink Dungeon Candle
Blue Dungeon Vase
Green Dungeon Vase
Pink Dungeon Vase
Blue Dungeon Door
Green Dungeon Door
Pink Dungeon Door
Blue Dungeon Bookcase
Green Dungeon Bookcase
Pink Dungeon Bookcase
Catacomb
Dungeon Shelf
Skellington J Skellingsworth
The Cursed Man
The Eye Sees the End
Something Evil is Watching You
The Twins Have Awoken
The Screamer
Goblins Playing Poker
Dryadisque
Sunflowers
Terrarian Gothic
Beanie
Imbuing Station
Star in a Bottle
Empty Bullet
Impact
Powered by Birds
The Persistency of Eyes
Unicorn Crossing the Hallows
Great Wave
Starry Night
Guide Picasso
The Guardian's Gaze
Father of Someone
Nurse Lisa
Shadowbeam Staff
Inferno Fork
Spectre Staff
Wooden Fence
Lead Fence
Bubble Machine
Bubble Wand
Marching Bones Banner
Necromantic Sign
Rusted Company Standard
Ragged Brotherhood Sigil
Molten Legion Flag
Diabolic Sigil
Obsidian Platform
Obsidian Door
Obsidian Chair
Obsidian Table
Obsidian Work Bench
Obsidian Vase
Obsidian Bookcase
Hellbound Banner
Hell Hammer Banner
Helltower Banner
Lost Hopes of Man Banner
Obsidian Watcher Banner
Lava Erupts Banner
Blue Dungeon Bed
Green Dungeon Bed
Pink Dungeon Bed
Obsidian Bed
Waldo
Dark Soul Reaper
Land
Trapped Ghost
Demon's Eye
Finding Gold
First Encounter
Good Morning
Underground Reward
Through the Window
Place Above the Clouds
Do Not Step on the Grass
Cold Waters in the White Land
Lightless Chasms
The Land of Deceiving Looks
Daylight
Secret of the Sands
Deadland Comes Alive
Evil Presence
Sky Guardian
American Explosive
Discover
Hand Earth
Old Miner
Skelehead
Facing the Cerebral Mastermind
Lake of Fire
Trio Super Heroes
Spectre Hood
Spectre Robe
Spectre Pants
Spectre Pickaxe
Spectre Hamaxe
Ectoplasm
Gothic Chair
Gothic Table
Gothic Work Bench
Gothic Bookcase
Paladin's Hammer
SWAT Helmet
Bee Wings
Giant Harpy Feather
Bone Feather
Fire Feather
Ice Feather
Broken Bat Wing
Tattered Bee Wing
Large Amethyst
Large Topaz
Large Sapphire
Large Emerald
Large Ruby
Large Diamond
Jungle Chest
Corruption Chest
Crimson Chest
Hallowed Chest
Frozen Chest
Jungle Key
Corruption Key
Crimson Key
Hallowed Key
Frozen Key
Imp Face
Ominous Presence
Shining Moon
Living Gore
Flowing Magma
Spectre Paintbrush
Spectre Paint Roller
Spectre Paint Scraper
Shroomite Headgear
Shroomite Mask
Shroomite Helmet
Shroomite Breastplate
Shroomite Leggings
Autohammer
Shroomite Bar
S.D.M.G.
Cenx's Tiara
Cenx's Breastplate
Cenx's Leggings
Crowno's Mask
Crowno's Breastplate
Crowno's Leggings
Will's Helmet
Will's Breastplate
Will's Leggings
Jim's Helmet
Jim's Breastplate
Jim's Leggings
Aaron's Helmet
Aaron's Breastplate
Aaron's Leggings
Vampire Knives
Broken Hero Sword
Scourge of the Corruptor
Staff of the Frost Hydra
The Creation of the Guide
The Merchant
Crowno Devours His Lunch
Rare Enchantment
Glorious Night
Sweetheart Necklace
Flurry Boots
D-Town's Helmet
D-Town's Breastplate
D-Town's Leggings
D-Town's Wings
Will's Wings
Crowno's Wings
Cenx's Wings
Cenx's Dress
Cenx's Dress Pants
Palladium Column
Palladium Column Wall
Bubblegum Block
Bubblegum Block Wall
Titanstone Block
Titanstone Block Wall
Magic Cuffs
Music Box (Snow)
Music Box (Space)
Music Box (Crimson)
Music Box (Boss 4)
Music Box (Alt Overworld Day)
Music Box (Rain)
Music Box (Ice)
Music Box (Desert)
Music Box (Ocean)
Music Box (Dungeon)
Music Box (Plantera)
Music Box (Boss 5)
Music Box (Temple)
Music Box (Eclipse)
Music Box (Mushrooms)
Butterfly Dust
Ankh Charm
Ankh Shield
Blue Flare
Angler Fish Banner
Angry Nimbus Banner
Anomura Fungus Banner
Antlion Banner
Arapaima Banner
Armored Skeleton Banner
Cave Bat Banner
Bird Banner
Black Recluse Banner
Blood Feeder Banner
Blood Jelly Banner
Blood Crawler Banner
Bone Serpent Banner
Bunny Banner
Chaos Elemental Banner
Mimic Banner
Clown Banner
Corrupt Bunny Banner
Corrupt Goldfish Banner
Crab Banner
Crimera Banner
Crimson Axe Banner
Cursed Hammer Banner
Demon Banner
Demon Eye Banner
Derpling Banner
Eater of Souls Banner
Enchanted Sword Banner
Zombie Eskimo Banner
Face Monster Banner
Floaty Gross Banner
Flying Fish Banner
Flying Snake Banner
Frankenstein Banner
Fungi Bulb Banner
Fungo Fish Banner
Gastropod Banner
Goblin Thief Banner
Goblin Sorcerer Banner
Goblin Peon Banner
Goblin Scout Banner
Goblin Warrior Banner
Goldfish Banner
Harpy Banner
Hellbat Banner
Herpling Banner
Hornet Banner
Ice Elemental Banner
Icy Merman Banner
Fire Imp Banner
Blue Jellyfish Banner
Jungle Creeper Banner
Lihzahrd Banner
Man Eater Banner
Meteor Head Banner
Moth Banner
Mummy Banner
Mushi Ladybug Banner
Parrot Banner
Pigron Banner
Piranha Banner
Pirate Deckhand Banner
Pixie Banner
Raincoat Zombie Banner
Reaper Banner
Shark Banner
Skeleton Banner
Dark Caster Banner
Blue Slime Banner
Snow Flinx Banner
Wall Creeper Banner
Spore Zombie Banner
Swamp Thing Banner
Giant Tortoise Banner
Toxic Sludge Banner
Umbrella Slime Banner
Unicorn Banner
Vampire Banner
Vulture Banner
Nymph Banner
Werewolf Banner
Wolf Banner
World Feeder Banner
Worm Banner
Wraith Banner
Wyvern Banner
Zombie Banner
Glass Platform
Glass Chair
Golden Chair
Golden Toilet
Bar Stool
Honey Chair
Steampunk Chair
"Glass Door"
"Golden Door"
"Honey Door"
"Steampunk Door"
"Glass Table"
"Banquet Table"
"Bar"
"Golden Table"
"Honey Table"
"Steampunk Table"
"Glass Bed"
"Golden Bed"
"Honey Bed"
"Steampunk Bed"
"Living Wood Wall"
"Fart in a Jar"
"Pumpkin"
"Pumpkin Wall"
"Hay"
"Hay Wall"
"Spooky Wood"
"Spooky Wood Wall"
"Pumpkin Helmet"
"Pumpkin Breastplate"
"Pumpkin Leggings"
"Candy Apple"
"Soul Cake"
"Nurse Hat"
"Nurse Shirt"
"Nurse Pants"
"Wizard's Hat"
"Guy Fawkes Mask"
"Dye Trader Robe"
"Steampunk Goggles"
"Cyborg Helmet"
"Cyborg Shirt"
"Cyborg Pants"
"Creeper Mask"
"Creeper Shirt"
"Creeper Pants"
"Cat Mask"
"Cat Shirt"
"Cat Pants"
"Ghost Mask"
"Ghost Shirt"
"Pumpkin Mask"
"Pumpkin Shirt"
"Pumpkin Pants"
"Robot Mask"
"Robot Shirt"
"Robot Pants"
"Unicorn Mask"
"Unicorn Shirt"
"Unicorn Pants"
"Vampire Mask"
"Vampire Shirt"
"Vampire Pants"
"Witch Hat"
"Leprechaun Hat"
"Leprechaun Shirt"
"Leprechaun Pants"
"Pixie Shirt"
"Pixie Pants"
"Princess Hat"
"Goodie Bag"
"Witch Dress"
"Witch Boots"
"Bride of Frankenstein Mask"
"Bride of Frankenstein Dress"
"Karate Tortoise Mask"
"Karate Tortoise Shirt"
"Karate Tortoise Pants"
"Candy Corn Rifle"
"Candy Corn"
"Jack 'O Lantern Launcher"
"Explosive Jack 'O Lantern"
"Sickle"
"Pumpkin Pie"
"Scarecrow Hat"
"Scarecrow Shirt"
"Scarecrow Pants"
"Cauldron"
"Pumpkin Chair"
"Pumpkin Door"
"Pumpkin Table"
"Pumpkin Work Bench"
"Pumpkin Platform"
"Tattered Fairy Wings"
"Spider Egg"
"Magical Pumpkin Seed"
"Bat Hook"
"Bat Scepter"
"Raven Staff"
"Jungle Key Mold"
"Corruption Key Mold"
"Crimson Key Mold"
"Hallowed Key Mold"
"Frozen Key Mold"
"Hanging Jack 'O Lantern"
"Rotten Egg"
"Unlucky Yarn"
"Black Fairy Dust"
"Jackelier"
"Jack 'O Lantern"
"Spooky Chair"
"Spooky Door"
"Spooky Table"
"Spooky Work Bench"
"Spooky Platform"
"Reaper Hood"
"Reaper Robe"
"Fox Mask"
"Fox Shirt"
"Fox Pants"
"Cat Ears"
"Bloody Machete"
"The Horseman's Blade"
"Bladed Glove"
"Pumpkin Seed"
"Spooky Hook"
"Spooky Wings"
"Spooky Twig"
"Spooky Helmet"
"Spooky Breastplate"
"Spooky Leggings"
"Stake Launcher"
"Stake"
"Cursed Sapling"
"Space Creature Mask"
"Space Creature Shirt"
"Space Creature Pants"
"Wolf Mask"
"Wolf Shirt"
"Wolf Pants"
"Pumpkin Moon Medallion"
"Necromantic Scroll"
"Jacking Skeletron"
"Bitter Harvest"
"Blood Moon Countess"
"Hallow's Eve"
"Morbid Curiosity"
"Treasure Hunter Shirt"
"Treasure Hunter Pants"
"Dryad Coverings"
"Dryad Loincloth"
"Mourning Wood Trophy"
"Pumpking Trophy"
"Jack 'O Lantern Mask"
"Sniper Scope"
"Heart Lantern": "a heart lantern is made with a life crystal and 4 chain",
"Jellyfish Diving Gear"
"Arctic Diving Gear"
"Frostspark Boots"
"Fart in a Balloon"
"Papyrus Scarab"
"Celestial Stone"
"Hoverboard"
"Candy Cane"
"Sugar Plum"
"Present"
"Red Ryder"
"Festive Wings"
"Pine Tree Block"
"Christmas Tree"
"Star Topper 1"
"Star Topper 2"
"Star Topper 3"
"Bow Topper"
"White Garland"
"White and Red Garland"
"Red Garland"
"Red and Green Garland"
"Green Garland"
"Green and White Garland"
"Multicolored Bulb"
"Red Bulb"
"Yellow Bulb"
"Green Bulb"
"Red and Green Bulb"
"Yellow and Green Bulb"
"Red and Yellow Bulb"
"White Bulb"
"White and Red Bulb"
"White and Yellow Bulb"
"White and Green Bulb"
"Multicolored Lights"
"Red Lights"
"Green Lights"
"Blue Lights"
"Yellow Lights"
"Red and Yellow Lights"
"Red and Green Lights"
"Yellow and Green Lights"
"Blue and Green Lights"
"Red and Blue Lights"
"Blue and Yellow Lights"
"Giant Bow"
"Reindeer Antlers"
"Holly"
"Candy Cane Sword"
"Elf Melter"
"Christmas Pudding"
"Eggnog"
"Star Anise"
"Reindeer Bells"
"Candy Cane Hook"
"Christmas Hook"
"Candy Cane Pickaxe"
"Fruitcake Chakram"
"Sugar Cookie"
"Gingerbread Cookie"
"Hand Warmer"
"Coal"
"Toolbox"
"Pine Door"
"Pine Chair"
"Pine Table"
"Dog Whistle"
"Christmas Tree Sword"
"Chain Gun"
"Razorpine
"Blizzard Staff
"Mrs. Claus Hat
"Mrs. Claus Shirt
"Mrs. Claus Heels
"Parka Hood
"Parka Coat
"Parka Pants
"Snow Hat
"Ugly Sweater
"Tree Mask
"Tree Shirt
"Tree Trunks
"Elf Hat
"Elf Shirt
"Elf Pants
"Snowman Cannon
"North Pole
"Christmas Tree Wallpaper
"Ornament Wallpaper
"Candy Cane Wallpaper
"Festive Wallpaper
"Stars Wallpaper
"Squiggles Wallpaper
"Snowflake Wallpaper
"Krampus Horn Wallpaper
"Bluegreen Wallpaper
"Grinch Finger Wallpaper
"Naughty Present
"Baby Grinch's Mischief Whistle
"Ice Queen Trophy
"Santa-NK1 Trophy
"Everscream Trophy
"Music Box (Pumpkin Moon)
"Music Box (Alt Underground)
"Music Box (Frost Moon)
"Brown Paint
"Shadow Paint
"Negative Paint
"Team Dye
"Amethyst Gemspark Block
"Topaz Gemspark Block
"Sapphire Gemspark Block
"Emerald Gemspark Block
"Ruby Gemspark Block
"Diamond Gemspark Block
"Amber Gemspark Block
"Life Hair Dye
"Mana Hair Dye
"Depth Hair Dye
"Money Hair Dye
"Time Hair Dye
"Team Hair Dye
"Biome Hair Dye
"Party Hair Dye
"Rainbow Hair Dye
"Speed Hair Dye
"Angel Halo
"Fez
"Womannequin
"Hair Dye Remover
"Bug Net
"Firefly
"Firefly in a Bottle
"Monarch Butterfly
"Purple Emperor Butterfly
"Red Admiral Butterfly
"Ulysses Butterfly
"Sulphur Butterfly
"Tree Nymph Butterfly
"Zebra Swallowtail Butterfly
"Julia Butterfly
"Worm
"Mouse
"Lightning Bug
"Lightning Bug in a Bottle
"Snail
"Glowing Snail
"Fancy Gray Wallpaper
"Ice Floe Wallpaper
"Music Wallpaper
"Purple Rain Wallpaper
"Rainbow Wallpaper
"Sparkle Stone Wallpaper
"Starlit Heaven Wallpaper
"Bird
"Blue Jay
"Cardinal
"Squirrel
"Bunny
"Cactus Bookcase
"Ebonwood Bookcase
"Flesh Bookcase
"Honey Bookcase
"Steampunk Bookcase
"Glass Bookcase
"Rich Mahogany Bookcase
"Pearlwood Bookcase
"Spooky Bookcase
"Skyware Bookcase
"Lihzahrd Bookcase
"Frozen Bookcase
"Cactus Lantern
"Ebonwood Lantern
"Flesh Lantern
"Honey Lantern
"Steampunk Lantern
"Glass Lantern
"Rich Mahogany Lantern
"Pearlwood Lantern
"Frozen Lantern
"Lihzahrd Lantern
"Skyware Lantern
"Spooky Lantern
"Frozen Door
"Cactus Candle
"Ebonwood Candle
"Flesh Candle
"Glass Candle
"Frozen Candle
"Rich Mahogany Candle
"Pearlwood Candle
"Lihzahrd Candle
"Skyware Candle
"Pumpkin Candle
"Cactus Chandelier
"Ebonwood Chandelier
"Flesh Chandelier
"Honey Chandelier
"Frozen Chandelier
"Rich Mahogany Chandelier
"Pearlwood Chandelier
"Lihzahrd Chandelier
"Skyware Chandelier
"Spooky Chandelier
"Glass Chandelier
"Cactus Bed
"Flesh Bed
"Frozen Bed
"Lihzahrd Bed
"Skyware Bed
"Spooky Bed
"Cactus Bathtub
"Ebonwood Bathtub
"Flesh Bathtub
"Glass Bathtub
"Frozen Bathtub
"Rich Mahogany Bathtub
"Pearlwood Bathtub
"Lihzahrd Bathtub
"Skyware Bathtub
"Spooky Bathtub
"Cactus Lamp
"Ebonwood Lamp
"Flesh Lamp
"Glass Lamp
"Frozen Lamp
"Rich Mahogany Lamp
"Pearlwood Lamp
"Lihzahrd Lamp
"Skyware Lamp
"Spooky Lamp
"Cactus Candelabra
"Ebonwood Candelabra
"Flesh Candelabra
"Honey Candelabra
"Steampunk Candelabra
"Glass Candelabra
"Rich Mahogany Candelabra
"Pearlwood Candelabra
"Frozen Candelabra
"Lihzahrd Candelabra
"Skyware Candelabra
"Spooky Candelabra
"Brain of Cthulhu Mask
"Wall of Flesh Mask
"Twin Mask
"Skeletron Prime Mask
"Plantera Mask
"Golem Mask
"Eater of Worlds Mask
"Eye of Cthulhu Mask
"Destroyer Mask
"Blacksmith Rack
"Carpentry Rack
"Helmet Rack
"Spear Rack
"Sword Rack
"Stone Slab
"Sandstone Slab
"Frog
"Mallard Duck
"Duck
"Honey Bathtub
"Steampunk Bathtub
"Living Wood Bathtub
"Shadewood Bathtub
"Bone Bathtub
"Honey Lamp
"Steampunk Lamp
"Living Wood Lamp
"Shadewood Lamp
"Golden Lamp
"Bone Lamp
"Living Wood Bookcase
"Shadewood Bookcase
"Golden Bookcase
"Bone Bookcase
"Living Wood Bed
"Bone Bed
"Living Wood Chandelier
"Shadewood Chandelier
"Golden Chandelier
"Bone Chandelier
"Living Wood Lantern
"Shadewood Lantern
"Golden Lantern
"Bone Lantern
"Living Wood Candelabra
"Shadewood Candelabra
"Golden Candelabra
"Bone Candelabra
"Living Wood Candle
"Shadewood Candle
"Golden Candle
"Black Scorpion
"Scorpion
"Bubble Wallpaper
"Copper Pipe Wallpaper
"Ducky Wallpaper
"Frost Core
"Bunny Cage
"Squirrel Cage
"Mallard Duck Cage
"Duck Cage
"Bird Cage
"Blue Jay Cage
"Cardinal Cage
"Waterfall Wall
"Lavafall Wall
"Crimson Seeds
"Heavy Work Bench
"Copper Plating
"Snail Cage
"Glowing Snail Cage
"Shroomite Digging Claw
"Ammo Box
"Monarch Butterfly Jar
"Purple Emperor Butterfly Jar
"Red Admiral Butterfly Jar
"Ulysses Butterfly Jar
"Sulphur Butterfly Jar
"Tree Nymph Butterfly Jar
"Zebra Swallowtail Butterfly Jar
"Julia Butterfly Jar
"Scorpion Cage
"Black Scorpion Cage
"Venom Staff
"Spectre Mask
"Frog Cage
"Mouse Cage
"Bone Welder
"Flesh Cloning Vat
"Glass Kiln
"Lihzahrd Furnace
"Living Loom
"Sky Mill
"Ice Machine
"Beetle Helmet
"Beetle Scale Mail
"Beetle Shell
"Beetle Leggings
"Steampunk Boiler
"Honey Dispenser
"Penguin
"Penguin Cage
"Worm Cage
"Terrarium
"Super Mana Potion
"Ebonwood Fence
"Rich Mahogany Fence
"Pearlwood Fence
"Shadewood Fence
"Brick Layer
"Extendo Grip
"Paint Sprayer
"Portable Cement Mixer
"Beetle Husk
"Celestial Magnet
"Celestial Emblem
"Celestial Cuffs
"Peddler's Hat
"Pulse Bow
"Large Dynasty Lantern
"Dynasty Lamp
"Dynasty Lantern
"Large Dynasty Candle
"Dynasty Chair
"Dynasty Work Bench
"Dynasty Chest
"Dynasty Bed
"Dynasty Bathtub
"Dynasty Bookcase
"Dynasty Cup
"Dynasty Bowl
"Dynasty Candle
"Dynasty Clock
"Golden Clock
"Glass Clock
"Honey Clock
"Steampunk Clock
"Fancy Dishes
"Glass Bowl
"Wine Glass
"Living Wood Piano
"Flesh Piano
"Frozen Piano
"Frozen Table
"Honey Chest
"Steampunk Chest
"Honey Work Bench
"Frozen Work Bench
"Steampunk Work Bench
"Glass Piano
"Honey Piano
"Steampunk Piano
"Honey Cup
"Chalice
"Dynasty Table
"Dynasty Wood
"Red Dynasty Shingles
"Blue Dynasty Shingles
"White Dynasty Wall
"Blue Dynasty Wall
"Dynasty Door
"Sake
"Pad Thai
"Pho
"Revolver
"Gatligator
"Arcane Rune Wall
"Water Gun
"Katana
"Ultrabright Torch
"Magic Hat
"Diamond Ring
"Gi
"Kimono
"Gypsy Robe
"Beetle Wings
"Tiger Skin
"Leopard Skin
"Zebra Skin
"Crimson Cloak
"Mysterious Cape
"Red Cape
"Winter Cape
"Frozen Chair
"Wood Fishing Pole
"Bass
"Reinforced Fishing Pole
"Fiberglass Fishing Pole
"Fisher of Souls
"Golden Fishing Rod
"Mechanic's Rod
"Sitting Duck's Fishing Pole
"Trout
"Salmon
"Atlantic Cod
"Tuna
"Red Snapper
"Neon Tetra
"Armored Cavefish
"Damselfish
"Crimson Tigerfish
"Frost Minnow
"Princess Fish
"Golden Carp
"Specular Fish
"Prismite
"Variegated Lardfish
"Flarefin Koi
"Double Cod
"Honeyfin
"Obsidifish
"Shrimp
"Chaos Fish
"Ebonkoi
"Hemopiranha
"Rockfish
"Stinkfish
"Mining Potion
"Heartreach Potion
"Calming Potion
"Builder Potion
"Titan Potion
"Flipper Potion
"Summoning Potion
"Dangersense Potion
"Purple Clubberfish
"Obsidian Swordfish
"Swordfish
"Iron Fence
"Wooden Crate
"Iron Crate
"Golden Crate
"Old Shoe
"Tin Can
"Minecart Track
"Reaver Shark
"Sawtooth Shark
"Minecart
"Ammo Reservation Potion
"Lifeforce Potion
"Endurance Potion
"Rage Potion
"Inferno Potion
"Wrath Potion
"Recall Potion
"Teleportation Potion
"Love Potion
"Stink Potion
"Fishing Potion
"Sonar Potion
"Crate Potion
"Shiverthorn Seeds
"Shiverthorn
"Warmth Potion
"Fish Hook
"Bee Headgear
"Bee Breastplate
"Bee Greaves
"Hornet Staff
"Imp Staff
"Queen Spider Staff
"Angler Hat
"Angler Vest
"Angler Pants
"Spider Mask
"Spider Breastplate
"Spider Greaves
"High Test Fishing Line
"Angler Earring
"Tackle Box
"Blue Dungeon Piano
"Green Dungeon Piano
"Pink Dungeon Piano
"Golden Piano
"Obsidian Piano
"Bone Piano
"Cactus Piano
"Spooky Piano
"Skyware Piano
"Lihzahrd Piano
"Blue Dungeon Dresser
"Green Dungeon Dresser
"Pink Dungeon Dresser
"Golden Dresser
"Obsidian Dresser
"Bone Dresser
"Cactus Dresser
"Spooky Dresser
"Skyware Dresser
"Honey Dresser
"Lihzahrd Dresser
"Sofa
"Ebonwood Sofa
"Rich Mahogany Sofa
"Pearlwood Sofa
"Shadewood Sofa
"Blue Dungeon Sofa
"Green Dungeon Sofa
"Pink Dungeon Sofa
"Golden Sofa
"Obsidian Sofa
"Bone Sofa
"Cactus Sofa
"Spooky Sofa
"Skyware Sofa
"Honey Sofa
"Steampunk Sofa
"Mushroom Sofa
"Glass Sofa
"Pumpkin Sofa
"Lihzahrd Sofa
"Seashell Hairpin
"Mermaid Adornment
"Mermaid Tail
"Zephyr Fish
"Fleshcatcher
"Hotline Fishing Hook
"Frog Leg
"Anchor
"Cooked Fish
"Cooked Shrimp
"Sashimi
"Fuzzy Carrot
"Scaly Truffle
"Slimy Saddle
"Bee Wax
"Copper Plating Wall
"Stone Slab Wall
"Sail
"Coralstone Block
"Blue Jellyfish Jar
"Green Jellyfish Jar
"Pink Jellyfish Jar
"Life Preserver
"Ship's Wheel
"Compass Rose
"Wall Anchor
"Goldfish Trophy
"Bunnyfish Trophy
"Swordfish Trophy
"Sharkteeth Trophy
"Batfish
"Bumblebee Tuna
"Catfish
"Cloudfish
"Cursedfish
"Dirtfish
"Dynamite Fish
"Eater of Plankton
"Fallen Starfish
"The Fish of Cthulhu
"Fishotron
"Harpyfish
"Hungerfish
"Ichorfish
"Jewelfish
"Mirage Fish
"Mutant Flinxfin
"Pengfish
"Pixiefish
"Spiderfish
"Tundra Trout
"Unicorn Fish
"Guide Voodoo Fish
"Wyverntail
"Zombie Fish
"Amanitia Fungifin
"Angelfish
"Bloody Manowar
"Bonefish
"Bunnyfish
"Cap'n Tunabeard
"Clownfish
"Demonic Hellfish
"Derpfish
"Fishron
"Infected Scabbardfish
"Mudfish
"Slimefish
"Tropical Barracuda
"King Slime Trophy
"Ship in a Bottle
"Hardy Saddle
"Pressure Plate Track
"King Slime Mask
"Fin Wings
"Treasure Map
"Seaweed Planter
"Pillagin Me Pixels
"Fish Costume Mask
"Fish Costume Shirt
"Fish Costume Finskirt
"Ginger Beard
"Honeyed Goggles
"Boreal Wood
"Palm Wood
"Boreal Wood Wall
"Palm Wood Wall
"Boreal Wood Fence
"Palm Wood Fence
"Boreal Wood Helmet
"Boreal Wood Breastplate
"Boreal Wood Greaves
"Palm Wood Helmet
"Palm Wood Breastplate
"Palm Wood Greaves
"Palm Wood Bow
"Palm Wood Hammer
"Palm Wood Sword
"Palm Wood Platform
"Palm Wood Bathtub
"Palm Wood Bed
"Palm Wood Bench
"Palm Wood Candelabra
"Palm Wood Candle
"Palm Wood Chair
"Palm Wood Chandelier
"Palm Wood Chest
"Palm Wood Sofa
"Palm Wood Door
"Palm Wood Dresser
"Palm Wood Lantern
"Palm Wood Piano
"Palm Wood Table
"Palm Wood Lamp
"Palm Wood Work Bench
"Optic Staff
"Palm Wood Bookcase
"Mushroom Bathtub
"Mushroom Bed
"Mushroom Bench
"Mushroom Bookcase
"Mushroom Candelabra
"Mushroom Candle
"Mushroom Chandelier
"Mushroom Chest
"Mushroom Dresser
"Mushroom Lantern
"Mushroom Lamp
"Mushroom Piano
"Mushroom Platform
"Mushroom Table
"Spider Staff
"Boreal Wood Bathtub
"Boreal Wood Bed
"Boreal Wood Bookcase
"Boreal Wood Candelabra
"Boreal Wood Candle
"Boreal Wood Chair
"Boreal Wood Chandelier
"Boreal Wood Chest
"Boreal Wood Clock
"Boreal Wood Door
"Boreal Wood Dresser
"Boreal Wood Lamp
"Boreal Wood Lantern
"Boreal Wood Piano
"Boreal Wood Platform
"Slime Bathtub
"Slime Bed
"Slime Bookcase
"Slime Candelabra
"Slime Candle
"Slime Chair
"Slime Chandelier
"Slime Chest
"Slime Clock
"Slime Door
"Slime Dresser
"Slime Lamp
"Slime Lantern
"Slime Piano
"Slime Platform
"Slime Sofa
"Slime Table
"Pirate Staff
"Slime Hook
"Sticky Grenade": "sticky grenade is made with a grenade and gel",
"Tartar Sauce
"Duke Fishron Mask
"Duke Fishron Trophy
"Molotov Cocktail
"Bone Clock
"Cactus Clock
"Ebonwood Clock
"Frozen Clock
"Lihzahrd Clock
"Living Wood Clock
"Rich Mahogany Clock
"Flesh Clock
"Mushroom Clock
"Obsidian Clock
"Palm Wood Clock
"Pearlwood Clock
"Pumpkin Clock
"Shadewood Clock
"Spooky Clock
"Skyware Clock
"Spider Fang
"Falcon Blade
"Fishron Wings
"Slime Gun
"Flairon
"Green Dungeon Chest
"Pink Dungeon Chest
"Blue Dungeon Chest
"Bone Chest
"Cactus Chest
"Flesh Chest
"Obsidian Chest
"Pumpkin Chest
"Spooky Chest
"Tempest Staff
"Razorblade Typhoon
"Bubble Gun
"Tsunami
"Seashell
"Starfish
"Steampunk Platform
"Skyware Platform
"Living Wood Platform
"Honey Platform
"Skyware Work Bench
"Glass Work Bench
"Living Wood Work Bench
"Flesh Sofa
"Frozen Sofa
"Living Wood Sofa
"Pumpkin Dresser
"Steampunk Dresser
"Glass Dresser
"Flesh Dresser
"Pumpkin Lantern
"Obsidian Lantern
"Pumpkin Lamp
"Obsidian Lamp"
"Blue Dungeon Lamp"
"Green Dungeon Lamp"
"Pink Dungeon Lamp"
"Honey Candle"
"Steampunk Candle"
"Spooky Candle"
"Obsidian Candle"
"Blue Dungeon Chandelier"
"Green Dungeon Chandelier"
"Pink Dungeon Chandelier"
"Steampunk Chandelier"
"Pumpkin Chandelier"
"Obsidian Chandelier"
"Blue Dungeon Bathtub"
"Green Dungeon Bathtub"
"Pink Dungeon Bathtub"
"Pumpkin Bathtub"
"Obsidian Bathtub"
"Golden Bathtub"
"Blue Dungeon Candelabra"
"Green Dungeon Candelabra"
"Pink Dungeon Candelabra"
"Obsidian Candelabra"
"Pumpkin Candelabra"
"Pumpkin Bed"
"Pumpkin Bookcase"
"Pumpkin Piano"
"Shark Statue"
"Truffle Worm"
"Apprentice Bait"
"Journeyman Bait"
"Master Bait"
"Amber Gemspark Wall"
"Offline Amber Gemspark Wall"
"Amethyst Gemspark Wall"
"Offline Amethyst Gemspark Wall"
"Diamond Gemspark Wall"
"Offline Diamond Gemspark Wall"
"Emerald Gemspark Wall"
"Offline Emerald Gemspark Wall"
"Ruby Gemspark Wall"
"Offline Ruby Gemspark Wall"
"Sapphire Gemspark Wall"
"Offline Sapphire Gemspark Wall"
"Topaz Gemspark Wall"
"Offline Topaz Gemspark Wall"
"Tin Plating Wall"
"Tin Plating"
"Waterfall Block"
"Lavafall Block"
"Confetti Block"
"Confetti Wall"
"Midnight Confetti Block"
"Midnight Confetti Wall"
"Weapon Rack"
"Fireworks Box"
"Living Fire Block"
"0' Statue"
"1' Statue"
"2' Statue"
"3' Statue"
"4' Statue"
"5' Statue"
"6' Statue"
"7' Statue"
"8' Statue"
"9' Statue"
"A' Statue"
"B' Statue"
"C' Statue"
"D' Statue"
"E' Statue"
"F' Statue"
"G' Statue"
"H' Statue"
"I' Statue"
"J' Statue"
"K' Statue"
"L' Statue"
"M' Statue"
"N' Statue"
"O' Statue"
"P' Statue"
"Q' Statue"
"R' Statue"
"S' Statue"
"T' Statue"
"U' Statue"
"V' Statue"
"W' Statue"
"X' Statue"
"Y' Statue"
"Z' Statue"
"Firework Fountain"
"Booster Track"
"Grasshopper"
"Grasshopper Cage"
"Music Box (Underground Crimson)"
"Cactus Table"
"Cactus Platform"
"Boreal Wood Sword"
"Boreal Wood Hammer"
"Boreal Wood Bow"
"Glass Chest"
"Xeno Staff"
"Meteor Staff"
"Living Cursed Fire Block"
"Living Demon Fire Block"
"Living Frost Fire Block"
"Living Ichor Fire Block"
"Living Ultrabright Fire Block"
"Gender Change Potion"
"Vortex Helmet"
"Vortex Breastplate"
"Vortex Leggings"
"Nebula Helmet"
"Nebula Breastplate"
"Nebula Leggings"
"Solar Flare Helmet"
"Solar Flare Breastplate"
"Solar Flare Leggings"
"Solar Tablet Fragment"
"Solar Tablet"
"Drill Containment Unit"
"Cosmic Car Key"
"Mothron Wings"
"Vortex Axe"
"Vortex Chainsaw"
"Vortex Drill"
"Vortex Hammer"
"Vortex Pickaxe"
"Nebula Axe"
"Nebula Chainsaw"
"Nebula Drill"
"Nebula Hammer"
"Nebula Pickaxe"
"Solar Flare Axe"
"Solar Flare Chainsaw"
"Solar Flare Drill"
"Solar Flare Hammer"
"Solar Flare Pickaxe"
"Honeyfall Block"
"Honeyfall Wall"
"Chlorophyte Brick Wall"
"Crimtane Brick Wall"
"Shroomite Plating Wall"
"Chlorophyte Brick"
"Crimtane Brick"
"Shroomite Plating"
"Laser Machinegun"
"Electrosphere Launcher"
"Xenopopper"
"Laser Drill"
"Mechanical Ruler"
"Anti-Gravity Hook"
"Moon Mask"
"Sun Mask"
"Martian Costume Mask"
"Martian Costume Shirt"
"Martian Costume Pants"
"Martian Uniform Helmet"
"Martian Uniform Torso"
"Martian Uniform Pants"
"Martian Astro Clock"
"Martian Bathtub"
"Martian Bed"
"Martian Hover Chair"
"Martian Chandelier"
"Martian Chest"
"Martian Door"
"Martian Dresser"
"Martian Holobookcase"
"Martian Hover Candle"
"Martian Lamppost"
"Martian Lantern"
"Martian Piano"
"Martian Platform"
"Martian Sofa"
"Martian Table"
"Martian Table Lamp"
"Martian Work Bench"
"Wooden Sink"
"Ebonwood Sink"
"Rich Mahogany Sink"
"Pearlwood Sink"
"Bone Sink"
"Flesh Sink"
"Living Wood Sink"
"Skyware Sink"
"Shadewood Sink"
"Lihzahrd Sink"
"Blue Dungeon Sink"
"Green Dungeon Sink"
"Pink Dungeon Sink"
"Obsidian Sink"
"Metal Sink"
"Glass Sink"
"Golden Sink"
"Honey Sink"
"Steampunk Sink"
"Pumpkin Sink"
"Spooky Sink"
"Frozen Sink"
"Dynasty Sink"
"Palm Wood Sink"
"Mushroom Sink"
"Boreal Wood Sink"
"Slime Sink"
"Cactus Sink"
"Martian Sink"
"Solar Cultist Hood"
"Lunar Cultist Hood"
"Solar Cultist Robe"
"Lunar Cultist Robe"
"Martian Conduit Plating"
"Martian Conduit Wall"
"HiTek Sunglasses"
"Martian Hair Dye"
"Martian Dye"
"Castle Marsberg"
"Martia Lisa"
"The Truth Is Up There"
"Smoke Block"
"Living Flame Dye"
"Living Rainbow Dye"
"Shadow Dye"
"Negative Dye"
"Living Ocean Dye"
"Brown Dye"
"Brown and Black Dye"
"Bright Brown Dye"
"Brown and Silver Dye"
"Wisp Dye"
"Pixie Dye"
"Influx Waver"
"Phasic Warp Ejector"
"Charged Blaster Cannon"
"Chlorophyte Dye"
"Unicorn Wisp Dye"
"Infernal Wisp Dye"
"Vicious Powder"
"Vicious Mushroom"
"The Bee's Knees"
"Gold Bird"
"Gold Bunny"
"Gold Butterfly"
"Gold Frog"
"Gold Grasshopper"
"Gold Mouse"
"Gold Worm"
"Sticky Dynamite"
"Angry Trapper Banner"
"Armored Viking Banner"
"Black Slime Banner"
"Blue Armored Bones Banner"
"Blue Cultist Archer Banner"
"Blue Cultist Caster Banner"
"Blue Cultist Fighter Banner"
"Bone Lee Banner"
"Clinger Banner"
"Cochineal Beetle Banner"
"Corrupt Penguin Banner"
"Corrupt Slime Banner"
"Corruptor Banner"
"Crimslime Banner"
"Cursed Skull Banner"
"Cyan Beetle Banner"
"Devourer Banner"
"Diabolist Banner"
"Doctor Bones Banner"
"Dungeon Slime Banner"
"Dungeon Spirit Banner"
"Elf Archer Banner"
"Elf Copter Banner"
"Eyezor Banner"
"Flocko Banner"
"Ghost Banner"
"Giant Bat Banner"
"Giant Cursed Skull Banner"
"Giant Flying Fox Banner"
"Gingerbread Man Banner"
"Goblin Archer Banner"
"Green Slime Banner"
"Headless Horseman Banner"
"Hell Armored Bones Banner"
"Hellhound Banner"
"Hoppin' Jack Banner"
"Ice Bat Banner"
"Ice Golem Banner"
"Ice Slime Banner"
"Ichor Sticker Banner"
"Illuminant Bat Banner"
"Illuminant Slime Banner"
"Jungle Bat Banner"
"Jungle Slime Banner"
"Krampus Banner"
"Lac Beetle Banner"
"Lava Bat Banner"
"Lava Slime Banner"
"Martian Brainscrambler Banner"
"Martian Drone Banner"
"Martian Engineer Banner"
"Martian Gigazapper Banner"
"Martian Gray Grunt Banner"
"Martian Officer Banner"
"Martian Raygunner Banner"
"Martian Scutlix Gunner Banner"
"Martian Tesla Turret Banner"
"Mister Stabby Banner"
"Mother Slime Banner"
"Necromancer Banner"
"Nutcracker Banner"
"Paladin Banner"
"Penguin Banner"
"Pinky Banner"
"Poltergeist Banner"
"Possessed Armor Banner"
"Present Mimic Banner"
"Purple Slime Banner"
"Ragged Caster Banner"
"Rainbow Slime Banner"
"Raven Banner"
"Red Slime Banner"
"Rune Wizard Banner"
"Rusty Armored Bones Banner"
"Scarecrow Banner"
"Scutlix Banner"
"Skeleton Archer Banner"
"Skeleton Commando Banner"
"Skeleton Sniper Banner"
"Slimer Banner"
"Snatcher Banner"
"Snow Balla Banner"
"Snowman Gangsta Banner"
"Spiked Ice Slime Banner"
"Spiked Jungle Slime Banner"
"Splinterling Banner"
"Squid Banner"
"Tactical Skeleton Banner"
"The Groom Banner"
"Tim Banner"
"Undead Miner Banner"
"Undead Viking Banner"
"White Cultist Archer Banner"
"White Cultist Caster Banner"
"White Cultist Fighter Banner"
"Yellow Slime Banner"
"Yeti Banner"
"Zombie Elf Banner"
"Sparky"
"Vine Rope"
"Wormhole Potion"
"Summoner Emblem"
"Bewitching Table"
"Alchemy Table"
"Strange Brew"
"Spelunker Glowstick"
"Bone Arrow"
"Bone Torch"
"Vine Rope Coil"
"Life Drain"
"Dart Pistol"
"Dart Rifle"
"Crystal Dart"
"Cursed Dart"
"Ichor Dart"
"Chain Guillotines"
"Fetid Baghnakhs"
"Clinger Staff"
"Putrid Scent"
"Flesh Knuckles"
"Flower Boots"
"Seedler"
"Hellwing Bow"
"Tendon Hook"
"Thorn Hook"
"Illuminant Hook"
"Worm Hook"
"Skiphs's Blood"
"Purple Ooze Dye"
"Reflective Silver Dye"
"Reflective Gold Dye"
"Blue Acid Dye"
"Daedalus Stormbow"
"Flying Knife"
"Bottomless Water Bucket"
"Super Absorbant Sponge"
"Gold Ring"
"Coin Ring"
"Greedy Ring"
"Fish Finder"
"Weather Radio"
"Hades Dye"
"Twilight Dye"
"Acid Dye"
"Glowing Mushroom Dye"
"Phase Dye"
"Magic Lantern"
"Music Box (Lunar Boss)"
"Rainbow Torch"
"Cursed Campfire"
"Demon Campfire"
"Frozen Campfire"
"Ichor Campfire"
"Rainbow Campfire"
"Crystal Vile Shard"
"Shadowflame Bow"
"Shadowflame Hex Doll"
"Shadowflame Knife"
"Cold Snap"
"Cursed Saint"
"Snowfellas"
"The Season"
"Bone Rattle"
"Architect Gizmo Pack"
"Meowmere"
"Enchanted Sundial"
"Star Wrath"
"Smooth Marble Block"
"Hellstone Brick Wall"
"Guide to Plant Fiber Cordage"
"Wand of Sparking"
"Gold Bird Cage"
"Gold Bunny Cage"
"Gold Butterfly Jar"
"Gold Frog Cage"
"Gold Grasshopper Cage"
"Gold Mouse Cage"
"Gold Worm Cage"
"Silk Rope"
"Web Rope"
"Silk Rope Coil"
"Web Rope Coil"
"Marble Block"
"Marble Wall"
"Smooth Marble Wall"
"Radar"
"Golden Lock Box"
"Granite Block"
"Smooth Granite Block"
"Granite Wall"
"Smooth Granite Wall"
"Royal Gel"
"Key of Night"
"Key of Light"
"Herb Bag"
"Javelin"
"Tally Counter"
"Sextant"
"Shield of Cthulhu"
"Butcher's Chainsaw"
"Stopwatch"
"Meteorite Brick"
"Meteorite Brick Wall"
"Metal Detector"
"Endless Quiver": "Made with 3996 wooden arrows in front of a crystal ball",
"Endless Musket Pouch"
"Toxic Flask"
"Psycho Knife"
"Nail Gun"
"Nail"
"Night Vision Helmet
"Celestial Shell"
"Pink Gel"
"Bouncy Glowstick"
"Pink Slime Block"
"Pink Torch"
"Bouncy Bomb"
"Bouncy Grenade"
"Peace Candle"
"Lifeform Analyzer"
"DPS Meter"
"Fisherman's Pocket Guide"
"Goblin Tech"
"R.E.K. 3000"
"PDA"
"Cell Phone"
"Granite Chest"
"Meteorite Clock"
"Marble Clock"
"Granite Clock"
"Meteorite Door"
"Marble Door"
"Granite Door"
"Meteorite Dresser"
"Marble Dresser"
"Granite Dresser"
"Meteorite Lamp"
"Marble Lamp"
"Granite Lamp"
"Meteorite Lantern"
"Marble Lantern"
"Granite Lantern"
"Meteorite Piano"
"Marble Piano"
"Granite Piano"
"Meteorite Platform"
"Marble Platform"
"Granite Platform"
"Meteorite Sink"
"Marble Sink"
"Granite Sink"
"Meteorite Sofa"
"Marble Sofa"
"Granite Sofa"
"Meteorite Table"
"Marble Table"
"Granite Table"
"Meteorite Work Bench"
"Marble Work Bench"
"Granite Work Bench"
"Meteorite Bathtub"
"Marble Bathtub"
"Granite Bathtub"
"Meteorite Bed"
"Marble Bed"
"Granite Bed"
"Meteorite Bookcase"
"Marble Bookcase"
"Granite Bookcase"
"Meteorite Candelabra"
"Marble Candelabra"
"Granite Candelabra"
"Meteorite Candle"
"Marble Candle"
"Granite Candle"
"Meteorite Chair"
"Marble Chair"
"Granite Chair"
"Meteorite Chandelier"
"Marble Chandelier"
"Granite Chandelier"
"Meteorite Chest"
"Marble Chest"
"Magic Water Dropper"
"Golden Bug Net"
"Magic Lava Dropper"
"Magic Honey Dropper"
"Empty Dropper"
"Gladiator Helmet"
"Gladiator Breastplate"
"Gladiator Leggings"
"Reflective Dye"
"Enchanted Nightcrawler"
"Grubby"
"Sluggy"
"Buggy"
"Grub Soup"
"Bomb Fish"
"Frost Daggerfish"
"Sharpening Station"
"Ice Mirror"
"Sailfish Boots"
"Tsunami in a Bottle"
"Target Dummy"
"Corrupt Crate"
"Crimson Crate"
"Dungeon Crate"
"Sky Crate"
"Hallowed Crate"
"Jungle Crate"
"Crystal Serpent"
"Toxikarp"
"Bladetongue"
"Shark Tooth Necklace"
"Money Trough"
"Bubble"
"Daybloom Planter Box"
"Moonglow Planter Box"
"Deathweed Planter Box"
"Blinkroot Planter Box"
"Waterleaf Planter Box"
"Shiverthorn Planter Box"
"Fireblossom Planter Box"
"Brain of Confusion"
"Worm Scarf"
"Balloon Pufferfish"
"Lazure's Valkyrie Circlet"
"Lazure's Valkyrie Cloak"
"Lazure's Barrier Platform"
"Golden Cross Grave Marker"
"Golden Tombstone"
"Golden Grave Marker"
"Golden Gravestone"
"Golden Headstone"
"Crystal Block"
"Music Box (Martian Madness)"
"Music Box (Pirate Invasion)"
"Music Box (Hell)"
"Crystal Block Wall"
"Trap Door"
"Tall Gate"
"Sharkron Balloon"
"Tax Collector's Hat"
"Tax Collector's Suit"
"Tax Collector's Pants"
"Bone Glove"
"Clothier's Jacket"
"Clothier's Pants"
"Dye Trader's Turban"
"Deadly Sphere Staff"
"Green Horseshoe Balloon"
"Amber Horseshoe Balloon"
"Pink Horseshoe Balloon"
"Lava Lamp"
"Enchanted Nightcrawler Cage"
"Buggy Cage"
"Grubby Cage"
"Sluggy Cage"
"Slap Hand"
"Twilight Hair Dye"
"Blessed Apple"
"Spectre Bar"
"Code 1"
"Buccaneer Bandana"
"Buccaneer Tunic"
"Buccaneer Pantaloons"
"Obsidian Outlaw Hat"
"Obsidian Longcoat"
"Obsidian Pants"
"Medusa Head"
"Item Frame"
"Sandstone Block"
"Hardened Sand Block"
"Sandstone Wall"
"Hardened Ebonsand Block"
"Hardened Crimsand Block"
"Ebonsandstone Block"
"Crimsandstone Block"
"Wooden Yoyo"
"Malaise"
"Artery"
"Amazon"
"Cascade"
"Chik"
"Code 2"
"Rally"
"Yelets"
"Red's Throw"
"Valkyrie Yoyo"
"Amarok"
"Hel-Fire"
"Kraken"
"The Eye of Cthulhu"
"Red String"
"Orange String"
"Yellow String"
"Lime String"
"Green String"
"Teal String"
"Cyan String"
"Sky Blue String"
"Blue String"
"Purple String"
"Violet String"
"Pink String"
"Brown String"
"White String"
"Rainbow String"
"Black String"
"Black Counterweight"
"Blue Counterweight"
"Green Counterweight"
"Purple Counterweight"
"Red Counterweight"
"Yellow Counterweight"
"Format C"
"Gradient"
"Valor"
"Hive Pack"
"Yoyo Glove"
"Demon Heart"
"Spore Sac"
"Shiny Stone"
"Hardened Pearlsand Block"
"Pearlsandstone Block"
"Hardened Sand Wall"
"Hardened Ebonsand Wall"
"Hardened Crimsand Wall"
"Hardened Pearlsand Wall"
"Ebonsandstone Wall"
"Crimsandstone Wall"
"Pearlsandstone Wall"
"Desert Fossil"
"Desert Fossil Wall"
"Exotic Scimitar"
"Paintball Gun"
"Classy Cane"
"Stylish Scissors"
"Mechanical Cart"
"Mechanical Wheel Piece"
"Mechanical Wagon Piece"
"Mechanical Battery Piece"
"Ancient Cultist Trophy"
"Martian Saucer Trophy"
"Flying Dutchman Trophy"
"Living Mahogany Wand"
"Rich Mahogany Leaf Wand"
"Fallen Tuxedo Shirt"
"Fallen Tuxedo Pants"
"Fireplace"
"Chimney"
"Yoyo Bag"
"Shrimpy Truffle"
"Arkhalis"
"Confetti Cannon"
"Music Box (The Towers)"
"Music Box (Goblin Invasion)"
"Ancient Cultist Mask"
"Moon Lord Mask"
"Fossil Helmet"
"Fossil Plate"
"Fossil Greaves"
"Amber Staff"
"Bone Javelin"
"Bone Throwing Knife"
"Sturdy Fossil"
"Stardust Helmet"
"Stardust Plate"
"Stardust Leggings"
"Portal Gun"
"Terrarian"
"Goblin Summoner Banner"
"Salamander Banner"
"Giant Shelly Banner"
"Crawdad Banner"
"Fritz Banner"
"Creature from the Deep Banner"
"Dr. Man Fly Banner"
"Mothron Banner"
"Severed Hand Banner"
"The Possessed Banner"
"Butcher Banner"
"Psycho Banner"
"Deadly Sphere Banner"
"Nailhead Banner"
"Poisonous Spore Banner"
"Medusa Banner"
"Hoplite Banner"
"Granite Elemental Banner"
"Grolem Banner"
"Blood Zombie Banner"
"Drippler Banner"
"Tomb Crawler Banner"
"Dune Splicer Banner"
"Antlion Swarmer Banner"
"Antlion Charger Banner"
"Ghoul Banner"
"Lamia Banner"
"Desert Spirit Banner"
"Basilisk Banner"
"Ravager Scorpion Banner"
"Stargazer Banner"
"Milkyway Weaver Banner"
"Flow Invader Banner"
"Twinkle Popper Banner"
"Small Star Cell Banner"
"Star Cell Banner"
"Corite Banner"
"Sroller Banner"
"Crawltipede Banner"
"Drakomire Rider Banner"
"Drakomire Banner"
"Selenian Banner"
"Predictor Banner"
"Brain Suckler Banner"
"Nebula Floater Banner"
"Evolution Beast Banner"
"Alien Larva Banner"
"Alien Queen Banner"
"Alien Hornet Banner"
"Vortexian Banner"
"Storm Diver Banner"
"Pirate Captain Banner"
"Pirate Deadeye Banner"
"Pirate Corsair Banner"
"Pirate Crossbower Banner"
"Martian Walker Banner"
"Red Devil Banner"
"Pink Jellyfish Banner"
"Green Jellyfish Banner"
"Dark Mummy Banner"
"Light Mummy Banner"
"Angry Bones Banner"
"Ice Tortoise Banner"
"Damage Booster"
"Life Booster"
"Mana Booster"
"Vortex Fragment"
"Nebula Fragment"
"Solar Fragment"
"Stardust Fragment"
"Luminite"
"Luminite Brick"
"Stardust Axe"
"Stardust Chainsaw"
"Stardust Drill"
"Stardust Hammer"
"Stardust Pickaxe"
"Luminite Bar"
"Solar Wings"
"Vortex Booster"
"Nebula Mantle"
"Stardust Wings"
"Luminite Brick Wall"
"Solar Eruption"
"Stardust Cell Staff"
"Vortex Beater"
"Nebula Arcanum"
"Blood Water"
"Wedding Veil"
"Wedding Dress"
"Platinum Bow"
"Platinum Hammer"
"Platinum Axe"
"Platinum Shortsword"
"Platinum Broadsword"
"Platinum Pickaxe"
"Tungsten Bow"
"Tungsten Hammer"
"Tungsten Axe"
"Tungsten Shortsword"
"Tungsten Broadsword"
"Tungsten Pickaxe"
"Lead Bow"
"Lead Hammer"
"Lead Axe"
"Lead Shortsword"
"Lead Broadsword"
"Lead Pickaxe"
"Tin Bow"
"Tin Hammer"
"Tin Axe"
"Tin Shortsword"
"Tin Broadsword"
"Tin Pickaxe"
"Copper Bow"
"Copper Hammer"
"Copper Axe"
"Copper Shortsword"
"Copper Broadsword"
"Copper Pickaxe"
"Silver Bow"
"Silver Hammer"
"Silver Axe"
"Silver Shortsword"
"Silver Broadsword"
"Silver Pickaxe"
"Gold Bow"
"Gold Hammer"
"Gold Axe"
"Gold Shortsword"
"Gold Broadsword"
"Gold Pickaxe"
"Solar Flare Hamaxe"
"Vortex Hamaxe"
"Nebula Hamaxe"
"Stardust Hamaxe"
"Solar Dye"
"Nebula Dye"
"Vortex Dye"
"Stardust Dye"
"Void Dye"
"Stardust Dragon Staff"
"Bacon"
"Shifting Sands Dye"
"Mirage Dye"
"Shifting Pearlsands Dye"
"Vortex Monolith"
"Nebula Monolith"
"Stardust Monolith"
"Solar Monolith"
"Phantasm"
"Last Prism"
"Nebula Blaze"
"Daybreak"
"Super Healing Potion"
"Detonator"
"Celebration"
"Bouncy Dynamite"
"Happy Grenade"
"Ancient Manipulator"
"Flame and Silver Dye"
"Green Flame and Silver Dye"
"Blue Flame and Silver Dye"
"Reflective Copper Dye"
"Reflective Obsidian Dye"
"Reflective Metal Dye"
"Midnight Rainbow Dye"
"Black and White Dye"
"Bright Silver Dye"
"Silver and Black Dye"
"Red Acid Dye"
"Gel Dye"
"Pink Gel Dye"
"Red Squirrel"
"Gold Squirrel"
"Red Squirrel Cage"
"Gold Squirrel Cage"
"Luminite Bullet"
"Luminite Arrow"
"Lunar Portal Staff"
"Lunar Flare"
"Rainbow Crystal Staff"
"Lunar Hook"
"Solar Fragment Block"
"Vortex Fragment Block"
"Nebula Fragment Block"
"Stardust Fragment Block"
"Suspicious Looking Tentacle"
"Yoraiz0r's Uniform"
"Yoraiz0r's Skirt"
"Yoraiz0r's Spell"
"Yoraiz0r's Scowl"
"Jim's Wings"
"Yoraiz0r's Recolored Goggles"
"Living Leaf Wall"
"Skiphs's Mask"
"Skiphs's Skin"
"Skiphs's Bear Butt"
"Skiphs's Paws"
"Loki's Helmet"
"Loki's Breastplate"
"Loki's Greaves"
"Loki's Wings"
"Sand Slime Banner"
"Sea Snail Banner"
"Moon Lord Trophy"
"Not a Kid, nor a Squid"
"Burning Hades Dye"
"Grim Dye"
"Loki's Dye"
"Shadowflame Hades Dye"
"Celestial Sigil"
"Logic Gate Lamp (Off)"
"Logic Gate (AND)"
"Logic Gate (OR)"
"Logic Gate (NAND)"
"Logic Gate (NOR)"
"Logic Gate (XOR)"
"Logic Gate (XNOR)"
"Conveyor Belt (Clockwise)"
"Conveyor Belt (Counter Clockwise)"
"The Grand Design"
"Yellow Wrench"
"Logic Sensor (Day)"
"Logic Sensor (Night)"
"Logic Sensor (Player Above)"
"Junction Box"
"Announcement Box"
"Logic Gate Lamp (On)"
"Mechanical Lens"
"Actuation Rod"
"Red Team Block"
"Red Team Platform"
"Static Hook"
"Presserator"
"Multicolor Wrench"
"Pink Weighted Pressure Plate"
"Engineering Helmet"
"Companion Cube"
"Wire Bulb"
"Orange Weighted Pressure Plate"
"Purple Weighted Pressure Plate"
"Cyan Weighted Pressure Plate"
"Green Team Block"
"Blue Team Block"
"Yellow Team Block"
"Pink Team Block"
"White Team Block"
"Green Team Platform"
"Blue Team Platform"
"Yellow Team Platform"
"Pink Team Platform"
"White Team Platform"
"Large Amber"
"Ruby Gem Lock"
"Sapphire Gem Lock"
"Emerald Gem Lock"
"Topaz Gem Lock"
"Amethyst Gem Lock"
"Diamond Gem Lock"
"Amber Gem Lock"
"Squirrel Statue"
"Butterfly Statue"
"Worm Statue"
"Firefly Statue"
"Scorpion Statue"
"Snail Statue"
"Grasshopper Statue"
"Mouse Statue"
"Duck Statue"
"Penguin Statue"
"Frog Statue"
"Buggy Statue"
"Logic Gate Lamp (Faulty)"
"Portal Gun Station"
"Trapped Chest"
"Trapped Gold Chest"
"Trapped Shadow Chest"
"Trapped Ebonwood Chest"
"Trapped Rich Mahogany Chest"
"Trapped Pearlwood Chest"
"Trapped Ivy Chest"
"Trapped Ice Chest"
"Trapped Living Wood Chest"
"Trapped Skyware Chest"
"Trapped Shadewood Chest"
"Trapped Web Covered Chest"
"Trapped Lihzahrd Chest"
"Trapped Water Chest"
"Trapped Jungle Chest"
"Trapped Corruption Chest"
"Trapped Crimson Chest"
"Trapped Hallowed Chest"
"Trapped Frozen Chest"
"Trapped Dynasty Chest"
"Trapped Honey Chest"
"Trapped Steampunk Chest"
"Trapped Palm Wood Chest"
"Trapped Mushroom Chest"
"Trapped Boreal Wood Chest"
"Trapped Slime Chest"
"Trapped Green Dungeon Chest"
"Trapped Pink Dungeon Chest"
"Trapped Blue Dungeon Chest"
"Trapped Bone Chest"
"Trapped Cactus Chest"
"Trapped Flesh Chest"
"Trapped Obsidian Chest"
"Trapped Pumpkin Chest"
"Trapped Spooky Chest"
"Trapped Glass Chest"
"Trapped Martian Chest"
"Trapped Meteorite Chest"
"Trapped Granite Chest"
"Trapped Marble Chest"
"Teal Pressure Pad"
"Wall Creeper Statue"
"Unicorn Statue"
"Drippler Statue"
"Wraith Statue"
"Bone Skeleton Statue"
"Undead Viking Statue"
"Medusa Statue"
"Harpy Statue"
"Pigron Statue"
"Hoplite Statue"
"Granite Golem Statue"
"Armed Zombie Statue"
"Blood Zombie Statue"
"Angler Tackle Bag"
"Geyser"
"Ultra Bright Campfire"
"Bone Campfire"
"Pixel Box"
"Liquid Sensor (Water)"
"Liquid Sensor (Lava)"
"Liquid Sensor (Honey)"
"Liquid Sensor (Any)"
"Bundled Party Balloons"
"Balloon Animal"
"Party Hat"
"Silly Sunflower Petals"
"Silly Sunflower Tops"
"Silly Sunflower Bottoms"
"Silly Pink Balloon"
"Silly Purple Balloon"
"Silly Green Balloon"
"Blue Streamer"
"Green Streamer"
"Pink Streamer"
"Silly Balloon Machine"
"Silly Tied Balloon (Pink)"
"Silly Tied Balloon (Purple)"
"Silly Tied Balloon (Green)"
"Pigronata"
"Party Center"
"Silly Tied Bundle of Balloons"
"Party Present"
"Slice of Cake"
"Cog Wall"
"Sandfall Wall"
"Snowfall Wall"
"Sandfall Block"
"Snowfall Block"
"Snow Cloud"
"Pedguin's Trousers"
"Silly Pink Balloon Wall"
"Silly Purple Balloon Wall"
"Silly Green Balloon Wall"
"0x33's Aviators"
"Blue Phasesaber"
"Red Phasesaber"
"Green Phasesaber"
"Purple Phasesaber"
"White Phasesaber"
"Yellow Phasesaber"
"Djinn's Curse"
"Ancient Horn"
"Mandible Blade"
"Ancient Headdress"
"Ancient Garments"
"Ancient Slacks"
"Forbidden Mask"
"Forbidden Robes"
"Forbidden Treads"
"Spirit Flame"
"Sand Elemental Banner"
"Pocket Mirror"
"Magic Sand Dropper"
"Forbidden Fragment"
"Lamia Tail"
"Lamia Wraps"
"Lamia Mask"
"Sky Fracture"
"Onyx Blaster"
"Sand Shark Banner"
"Bone Biter Banner"
"Flesh Reaver Banner"
"Crystal Thresher Banner"
"Angry Tumbler Banner"
"Ancient Cloth"
"Desert Spirit Lamp"
"Music Box (Sandstorm)"
"Apprentice's Hat"
"Apprentice's Robe"
"Apprentice's Trousers"
"Squire's Great Helm"
"Squire's Plating"
"Squire's Greaves"
"Huntress's Wig"
"Huntress's Jerkin"
"Huntress's Pants"
"Monk's Bushy Brow Bald Cap"
"Monk's Shirt"
"Monk's Pants"
"Apprentice's Scarf"
"Squire's Shield"
"Huntress's Buckler"
"Monk's Belt"
"Defender's Forge"
"War Table"
"War Table Banner"
"Eternia Crystal Stand"
"Defender Medal"
"Flameburst Rod"
"Flameburst Cane"
"Flameburst Staff"
"Ale Tosser"
"Etherian Mana"
"Brand of the Inferno"
"Ballista Rod"
"Ballista Cane"
"Ballista Staff"
"Flying Dragon"
"Eternia Crystal"
"Lightning Aura Rod"
"Lightning Aura Cane"
"Lightning Aura Staff"
"Explosive Trap Rod"
"Explosive Trap Cane"
"Explosive Trap Staff"
"Sleepy Octopod"
"Ghastly Glaive"
"Etherian Goblin Bomber Banner"
"Etherian Goblin Banner"
"Old One's Skeleton Banner"
"Drakin Banner"
"Kobold Glider Banner"
"Kobold Banner"
"Wither Beast Banner"
"Etherian Wyvern Banner"
"Etherian Javelin Thrower Banner"
"Etherian Lightning Bug Banner"
"Tome of Infinite Wisdom"
"Phantom Phoenix"
"Gato Egg"
"Creeper Egg"
"Dragon Egg"
"Sky Dragon's Fury"
"Aerial Bane"
"Treasure Bag (Betsy)"
"Treasure Bag (Dark Mage)"
"Treasure Bag (Ogre)"
"Betsy Mask"
"Dark Mage Mask"
"Ogre Mask"
"Betsy Trophy"
"Dark Mage Trophy"
"Ogre Trophy"
"Music Box (Old One's Army)"
"Betsy's Wrath"
"Valhalla Knight's Helm"
"Valhalla Knight's Breastplate"
"Valhalla Knight's Greaves"
"Dark Artist's Hat"
"Dark Artist's Robes"
"Dark Artist's Leggings"
"Red Riding Hood"
"Red Riding Dress"
"Red Riding Leggings"
"Shinobi Infiltrator's Helmet"
"Shinobi Infiltrator's Torso"
"Shinobi Infiltrator's Pants"
"Betsy's Wings"
"Dragon Mask"
"Titan Helmet"
"Spectral Headgear"
"Dragon Breastplate"
"Titan Mail"
"Spectral Armor"
"Dragon Greaves"
"Titan Leggings"
"Spectral Subligar"
"Tizona"
"Tonbogiri"
"Sharanga"
"Spectral Arrow"
"Vulcan Repeater"
"Vulcan Bolt"
"Suspicious Looking Skull"
"Soul of Blight"
"Petri Dish"
"Beeswax"
"Vial of Blood"
"Wolf Fang"
"Brain"
"Music Box (Desert)"
"Music Box (Space)"
"Music Box (Tutorial)"
"Music Box (Boss 4)"
"Music Box (Ocean)"
"Music Box (Snow)"
"Fabulous Ribbon"
"George's Hat"
"Fabulous Dress"
"George's Suit"
"Fabulous Slippers"
"George's Pants"
"Sparkly Wings"
"Ocram Trophy"
"Albino Antlion Banner"
"Orca Banner"
"Vampire Miner Banner"
"Shadow Hammer Banner"
"Shadow Mummy Banner"
"Spectral Gastropod Banner"
"Spectral Elemental Banner"
"Dragon Snatcher Banner"
"Arch Wyvern Banner"
"Arch Demon Banner"
"Holiday Bauble"
"Shiny Black Slab"
"Heart Arrow"
"Broken Heart Crystal"
"Valentine Ring"
"Rainbow Piece"
"Pot o' Gold"
"Mysterious Package"
"Golden Seaweed"
"Suspicious Looking Egg"
"Boots of Ostara"
"Egg Cannon"
"Suspicious Looking Apple"
"Old Walking Stick"
"Holy Hand Grenade"
"Strange Looking Tombstone"
"Turkey Feather"
"Cursed Stuffing"
"Horn 'o' Plenty"
"Roman Candle"
"Festive Top Hat"
"Alpine Hat"
"Lederweste"
"Lederhosen"
"Oktober Locks"
"Dirndl Blouse"
"Dirndl Skirt"
"Wiesnbräu"

}