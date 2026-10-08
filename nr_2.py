from pyblockworld import World

from wall import Wall


# Milestone 2: one normal and one rotated wall
def b_key_pressed(world: World):
    x, y, z = world.player_position(as_int=True)
    pos = (x + 3, y - 1, z + 3)  # a bit away, on the ground

    wall = Wall(pos, world)
    wall.build()

    rotated_wall = Wall(pos, world)
    rotated_wall.rotated = True
    rotated_wall.build()


world = World()  # only ONE World -> only one window
world.build_key_pressed = b_key_pressed
world.run()
