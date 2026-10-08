from roof import Roof
from wall import Wall, WallWithDoor, WallWithWindow


class House:
    def __init__(self, pos: tuple, bw):
        self.pos = pos
        self.__bw = bw  # private (-)
        x, y, z = pos

        self.wallFront = WallWithDoor(pos, bw)

        self.wallBack = Wall(pos, bw)
        self.wallBack.pos = (x, y, z + self.wallBack.width - 1)

        self.wallLeft = WallWithWindow(pos, bw)
        self.wallLeft.rotated = True

        self.wallRight = WallWithWindow(pos, bw)
        self.wallRight.rotated = True
        self.wallRight.pos = (x + self.wallRight.width - 1, y, z)

        # roof sits on top of the walls
        self.roof = Roof((x, y + self.wallFront.height, z), bw)

    def _walls(self):
        return [self.wallFront, self.wallLeft, self.wallRight, self.wallBack]

    def build(self):
        for wall in self._walls():
            wall.build()
        self.roof.build()

    def change_wall_material(self, new_material_id: str):
        """Change the material of all 4 walls. Call build() again to see it."""
        for wall in self._walls():
            wall.material_id = new_material_id
