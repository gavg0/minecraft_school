class Wall:
    def __init__(self, pos: tuple, bw):
        self.width = 6
        self.height = 5
        self.pos = pos
        self.rotated = False
        self.material_id = "default:stone"
        self._bw = bw  # protected (#): subclasses may use it

    def build(self):
        self._fill(0, 0, self.width - 1, self.height - 1, self.material_id)

    def _fill(self, a1, h1, a2, h2, material):
        """Fill a rectangle in wall coordinates: a = along the wall, h = height."""
        x, y, z = self.pos
        if self.rotated:
            # turned 90° around the y-axis -> runs along z
            self._bw.setBlocks(x, y + h1, z + a1, x, y + h2, z + a2, material)
        else:
            # runs along x
            self._bw.setBlocks(x + a1, y + h1, z, x + a2, y + h2, z, material)


class WallWithDoor(Wall):
    def __init__(self, pos: tuple, bw):
        super().__init__(pos, bw)  # sets width, height, ... from Wall
        self.door_material_id = "air"

    def build(self):
        super().build()  # solid wall first
        mid = self.width // 2
        self._fill(mid - 1, 0, mid, 2, self.door_material_id)  # 2 wide, 3 high


class WallWithWindow(Wall):
    def __init__(self, pos: tuple, bw):
        super().__init__(pos, bw)
        self.window_material_id = "air"

    def build(self):
        super().build()
        mid = self.width // 2
        self._fill(mid - 1, 2, mid, 3, self.window_material_id)  # 2x2, raised
