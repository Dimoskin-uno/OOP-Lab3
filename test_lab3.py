import unittest
from sea_boat import SeaBoat
class TestSeaBoat(unittest.TestCase):
    def setUp(self):
        self.boat1 = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        self.boat2 = SeaBoat("Neptune", 25.0, 60, 80, 2015)
        self.boat3 = SeaBoat("BlackSea", 40.2, 50, 200, 2008)
        self.boat4 = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
        self.boat5 = SeaBoat("Atlantis", 28.7, 48, 100, 2018)

        self.boats = [
            self.boat1,
            self.boat2,
            self.boat3,
            self.boat4,
            self.boat5
        ]

    def test_equality(self):
        boat_copy = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
        self.assertEqual(self.boat4, boat_copy)

    def test_inequality(self):
        self.assertNotEqual(self.boat1, self.boat2)

    def test_sort_by_length(self):
        self.boats.sort(key=lambda boat: (boat.length, -boat.speed))
        lengths = [boat.length for boat in self.boats]
        self.assertEqual(lengths, sorted(lengths))

    def test_sort_by_speed(self):
        self.boats.sort(key=lambda boat: (-boat.speed, boat.length))
        speeds = [boat.speed for boat in self.boats]
        self.assertEqual(speeds, sorted(speeds, reverse=True))

    def test_search_boat(self):
        target = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
        self.assertIn(target, self.boats)

if __name__ == "__main__":
    unittest.main()
