from turtle import width

from pyblockworld import World

world = World()

class wall:
    def __init__(self, width, height, pos, rotated, material_id,bw):
        self.width = width
        self.height = height
        self.pos = pos
        self.rotated = rotated
        self.material_id = material_id
        self._bw = bw

    def Wall(self):
        # Code to create a wall in Minecraft using the specified parameters
        world.setBlocks(self.pos[0], self.pos[1], self.pos[2],self.width, self.height, 1, self.material_id)

    def build(self):
        # Code to build the wall in Minecraft at the specified coordinates
        pass
