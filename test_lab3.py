import unittest
from sea_boat import SeaBoat, SeaFleet

class TestSeaBoat(unittest.TestCase):

    def test_init_stores_values(self):
        boat = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        self.assertEqual(boat.name, "Odessa")
        self.assertEqual(boat.length, 30.5)
        self.assertEqual(boat.speed, 45.0)
        self.assertEqual(boat.capacity, 120)
        self.assertEqual(boat.year, 2010)

    def test_private_fields_not_accessible(self):
        boat = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        self.assertFalse(hasattr(boat, "name_"))
        self.assertFalse(hasattr(boat, "_name"))
        with self.assertRaises(AttributeError):
            _ = boat.__name 

    def test_setter_updates_value(self):
        boat = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        boat.name = "  Kherson  "
        self.assertEqual(boat.name, "Kherson")

    def test_setter_rejects_empty_name(self):
        boat = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        with self.assertRaises(ValueError):
            boat.name = "   "

    def test_setter_rejects_invalid_speed(self):
        boat = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        with self.assertRaises(ValueError):
            boat.speed = -10

    def test_setter_rejects_invalid_year(self):
        boat = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        with self.assertRaises(ValueError):
            boat.year = 1700

    def test_init_rejects_invalid_speed(self):
        with self.assertRaises(ValueError):
            SeaBoat("X", 10.0, 0, 50, 2000)

    def test_init_rejects_invalid_year(self):
        with self.assertRaises(ValueError):
            SeaBoat("X", 10.0, 30, 50, 1799)
            
    def test_equality_identical_objects(self):
        boat = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
        copy = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
        self.assertEqual(boat, copy)

    def test_inequality_different_objects(self):
        boat1 = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        boat2 = SeaBoat("Neptune", 25.0, 60, 80, 2015)
        self.assertNotEqual(boat1, boat2)

    def test_equality_returns_not_implemented_for_wrong_type(self):
        boat = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        self.assertNotEqual(boat, "not a boat")
        self.assertNotEqual(boat, 42)

    def test_repr_contains_name(self):
        boat = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        self.assertIn("Odessa", repr(boat))

    def test_repr_roundtrip(self):
        boat = SeaBoat("Odessa", 30.5, 45.0, 120, 2010)
        self.assertEqual(
            repr(boat),
            "SeaBoat(name='Odessa', length=30.5, speed=45.0, capacity=120, year=2010)",
        )

class TestSeaFleet(unittest.TestCase):
    def setUp(self):
        self.fleet = SeaFleet()
        for name, length, speed, capacity, year in [
            ("Odessa",   30.5, 45, 120, 2010),
            ("Neptune",  25.0, 60,  80, 2015),
            ("BlackSea", 40.2, 50, 200, 2008),
            ("Poseidon", 35.0, 55, 150, 2012),
            ("Atlantis", 28.7, 48, 100, 2018),
        ]:
            self.fleet.add(SeaBoat(name, length, speed, capacity, year))

    def test_add_increases_length(self):
        before = len(self.fleet)
        self.fleet.add(SeaBoat("New", 20.0, 40, 50, 2020))
        self.assertEqual(len(self.fleet), before + 1)

    def test_add_rejects_non_boat(self):
        with self.assertRaises(TypeError):
            self.fleet.add("not a boat")

    def test_remove_existing_boat(self):
        target = SeaBoat("Odessa", 30.5, 45, 120, 2010)
        result = self.fleet.remove(target)
        self.assertTrue(result)
        self.assertEqual(len(self.fleet), 4)

    def test_remove_nonexistent_returns_false(self):
        ghost = SeaBoat("Ghost", 99.0, 99, 999, 2099)
        self.assertFalse(self.fleet.remove(ghost))

    def test_boats_property_returns_tuple(self):
        self.assertIsInstance(self.fleet.boats, tuple)

    def test_boats_property_is_copy(self):
        snapshot = self.fleet.boats
        self.fleet.add(SeaBoat("Extra", 10.0, 30, 20, 2021))
        self.assertEqual(len(snapshot), 5) 
        
    def test_sort_by_length_ascending(self):
        self.fleet.sort_by_length()
        lengths = [b.length for b in self.fleet]
        self.assertEqual(lengths, sorted(lengths))

    def test_sort_by_length_descending(self):
        self.fleet.sort_by_length(descending=True)
        lengths = [b.length for b in self.fleet]
        self.assertEqual(lengths, sorted(lengths, reverse=True))

    def test_sort_by_length_tiebreak_speed(self):
        """При однаковій довжині — вищий speed має йти першим."""
        fleet = SeaFleet()
        fleet.add(SeaBoat("Slow", 30.0, 40, 50, 2010))
        fleet.add(SeaBoat("Fast", 30.0, 70, 50, 2010))
        fleet.sort_by_length()
        self.assertEqual(fleet.boats[0].name, "Fast")

    def test_sort_by_speed_descending(self):
        self.fleet.sort_by_speed()
        speeds = [b.speed for b in self.fleet]
        self.assertEqual(speeds, sorted(speeds, reverse=True))

    def test_sort_by_speed_ascending(self):
        self.fleet.sort_by_speed(descending=False)
        speeds = [b.speed for b in self.fleet]
        self.assertEqual(speeds, sorted(speeds))

    def test_find_existing_boat(self):
        target = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
        result = self.fleet.find(target)
        self.assertIsNotNone(result)
        self.assertEqual(result, target)

    def test_find_nonexistent_returns_none(self):
        ghost = SeaBoat("Ghost", 99.0, 99, 999, 2099)
        self.assertIsNone(self.fleet.find(ghost))

    def test_len(self):
        self.assertEqual(len(self.fleet), 5)

    def test_iter(self):
        names = [b.name for b in self.fleet]
        self.assertEqual(len(names), 5)
        self.assertIn("Odessa", names)

    def test_repr(self):
        self.assertIn("5", repr(self.fleet))

if __name__ == "__main__":
    unittest.main()
