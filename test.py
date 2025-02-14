import unittest
from generator import generate_bicycles
import json
import random

class TestBicycleGenerator(unittest.TestCase):
    def test_generate_bicycles(self):
        file_path = "Bicycle.xlsx"
        output_json = generate_bicycles(file_path)
        bicycles = json.loads(output_json)
        
        self.assertIsInstance(bicycles, list)
        self.assertTrue(len(bicycles) > 0)

        random_bicycle = random.choice(bicycles)
        self.assertIn("ID", random_bicycle)
        self.assertIn("Manufacturer", random_bicycle)
        self.assertIn("Type", random_bicycle)
        self.assertIn("Frame type", random_bicycle)
        self.assertIn("Frame material", random_bicycle)

        self.assertEqual(random_bicycle["Manufacturer"], "Bikes INC")
        self.assertEqual(random_bicycle["Type"], "City")
        self.assertEqual(random_bicycle["Frame type"], "Diamond")
        self.assertEqual(random_bicycle["Frame material"], "Aluminum")

if __name__ == "__main__":
    unittest.main()
