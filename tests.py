import unittest

from info import Flights


class TestFlights(unittest.TestCase):
    def test_wrong_order_of_info(self):
        file_csv = 'data.csv'
        flight_id = 3
        flights = Flights(file_csv)
        right_order = flights.search(flight_id)
        wrong_order = '{"DepartureTime": "2010", "Number": "SU-275", "ArrivalTime": "1115"}'
        self.assertNotEqual(right_order, wrong_order)

    def test_id_not_found(self):
        file_csv = 'data.csv'
        flight_id = 5
        flights = Flights(file_csv)
        test_result = flights.search(flight_id)
        true_result = None
        self.assertEqual(test_result, true_result)
        
    def test_csv_file_not_found(self):
        file_csv = '1.csv'
        try:
            flights = Flights(file_csv)
        except FileNotFoundError:
            True
        
    def test_general_case(self):
        file_csv = 'data.csv'
        flight_id = 2
        flights = Flights(file_csv)
        test_result = flights.search(flight_id)
        true_result = '{"Number": "SU-275", "DepartureTime": "2010", "ArrivalTime": "1115"}'
        self.assertEqual(test_result, true_result)


if __name__ == "__main__":
    unittest.main()
