import unittest
from travel_app import TravelApp
import travel_app

def return_100(x):
    return "100"

class TestTravelApp(unittest.TestCase):

    def setUp(self):
        self.ta = TravelApp()
        
    def test_get_possible_destinations_based_on_budget(self):
        self.ta.user_budget = 1200
        self.ta.read_source_data()
        filtered_dests = self.ta.get_possible_destinations_based_on_budget()
        self.assertEqual(len(filtered_dests), 1)
        
    def test_get_user_dest(self):
        self.ta.user_budget = 1200
        self.ta.read_source_data()
        travel_app.input = lambda x: "Japan"
        self.ta.get_user_destination()
        self.assertEqual(self.ta.user_destination, "Japan")
        
    def test_get_user_budget(self):
        self.ta.get_user_budget(return_100)
        self.assertEqual(self.ta.user_budget, 100)
        

# Run the tests if this script is executed
if __name__ == '__main__':
    unittest.main()
