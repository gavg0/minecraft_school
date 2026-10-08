from pyblockworld import World


class Wall:
    def __init__(self, pos: tuple, bw: World):
        self.width = 6
        self.height = 5
        self.pos = pos
        self.rotated = False
        self.material_id = "default:stone"
        self._bw = bw  # protected (#)

    def build(self):
        x, y, z = self.pos
        top = y + self.height - 1
        if self.rotated:
            # turned 90° around the y-axis -> runs along z
            self._bw.setBlocks(x, y, z, x, top, z + self.width - 1, self.material_id)
        else:
            # runs along x
            self._bw.setBlocks(x, y, z, x + self.width - 1, top, z, self.material_id)
