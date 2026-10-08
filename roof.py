class Roof:
    def __init__(self, pos: tuple, bw):
        self.width = 6
        self.depth = 6
        self.roof_material_id = "default:brick"
        self.pos = pos
        self.__bw = bw  # private (-): only Roof itself

    def build(self):
        x, y, z = self.pos
        # flat roof: width along x, depth along z
        self.__bw.setBlocks(x, y, z, x + self.width - 1, y, z + self.depth - 1,
                            self.roof_material_id)
