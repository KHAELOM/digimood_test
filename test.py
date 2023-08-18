#NOT COMPLETE


import unittest
from Vessel import SupportCraft, OffensiveCraft

class TestShips(unittest.TestCase):

    def test_support_ship_creation(self):
        support_ship = SupportCraft("Support1", 100, (0, 0), "refueling")
        self.assertEqual(support_ship.name, "Support1")
        self.assertEqual(support_ship.max_health, 100)
        #TODO

    def test_offensive_ship_creation(self):
        offensive_ship = OffensiveCraft("Offensive1", 100, (0, 0), "battleship")
        self.assertEqual(offensive_ship.name, "Offensive1")
        self.assertEqual(offensive_ship.max_health, 100)
        #TODO

if __name__ == '__main__':
    unittest.main()