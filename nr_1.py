from pyblockworld import World


# Milestone 1: 3 blocks in x, 4 in y, 5 in z
def b_key_pressed(world: World):
    x, y, z = world.player_position(as_int=True)
    x += 2  # a bit away from the player
    y -= 1  # feet level (ground is at y = -2)

    # setBlocks(start corner, end corner) -> end = start + count - 1
    world.setBlocks(x, y, z,     x + 2, y,     z,     "default:brick")  # 3 in x
    world.setBlocks(x, y + 1, z, x,     y + 4, z,     "default:sand")   # 4 in y
    world.setBlocks(x, y, z + 1, x,     y,     z + 5, "default:stone")  # 5 in z


world = World()
world.build_key_pressed = b_key_pressed
world.run()
