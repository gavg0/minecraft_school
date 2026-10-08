import unittest
from unittest.mock import Mock

from house import House


class HouseTest(unittest.TestCase):
    def setUp(self):
        # Mock = stand-in for the World, no game window needed
        self.house = House((0, 0, 0), Mock())
        self.walls = [self.house.wallFront, self.house.wallLeft,
                      self.house.wallRight, self.house.wallBack]

    def test_change_wall_material(self):
        for wall in self.walls:
            self.assertEqual(wall.material_id, "default:stone")  # default

        self.house.change_wall_material("default:sand")

        for wall in self.walls:
            self.assertEqual(wall.material_id, "default:sand")
        # roof and door must stay unchanged
        self.assertEqual(self.house.roof.roof_material_id, "default:brick")
        self.assertEqual(self.house.wallFront.door_material_id, "air")


if __name__ == "__main__":
    unittest.main()
