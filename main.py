from pyblockworld import World

from house import House


# Milestone 6: B builds a whole house
def b_key_pressed(world: World):
    x, y, z = world.player_position(as_int=True)
    house = House((x + 3, y - 1, z + 3), world)
    house.build()


world = World()
world.build_key_pressed = b_key_pressed
world.run()
