from pyblockworld import World

import wall


# air, default:brick, default:stone, default:sand, default:grass
def b_key_pressed(world:World):
    print("Block types", World.MATERIALS)
    x,y,z = world.player_position()
    y=-1
    world.setBlocks(x,y,z, 3,-1,0, "default:grass")
    world.setBlocks(x,y,z, 0,3,0, "default:sand")
    world.setBlocks(x,y,z, 0,-1,3, "default:brick")

wall1 = wall.wall(5, 3, (0, 0, 0), False, "default:brick", World())
world = World()
# Die Funktion für die build-Taste (b) wird zugewiesen
world.build_key_pressed = b_key_pressed
world.run()

# Mehrere Blöcke auf einmal abseits des Spielers platzieren
#x,y,z = x,y,z+3
#world.setBlocks(x,y,z, x+3,y+3,z+3, "default:grass")

#world = World()
#world.build_key_pressed = b_key_pressed
#world.run()
