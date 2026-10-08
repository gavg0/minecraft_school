from pyblockworld import World

from wall import WallWithDoor, WallWithWindow


# Milestone 3: each wall type twice, one normal and one rotated
def b_key_pressed(world: World):
    x, y, z = world.player_position(as_int=True)
    y -= 1  # on the ground

    for wall_type, pos in [(WallWithWindow, (x + 3, y, z + 3)),
                           (WallWithDoor,   (x + 3, y, z - 8))]:
        normal = wall_type(pos, world)
        normal.build()

        rotated = wall_type(pos, world)
        rotated.rotated = True
        rotated.build()


world = World()
world.build_key_pressed = b_key_pressed
world.run()
