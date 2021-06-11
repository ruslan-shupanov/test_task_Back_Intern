import reader
import json


class Flights:
    def __init__(self, file_csv):
        self.data = reader.read_csv(file_csv)

    def search(self, flight_id):
        """Search for a flight Id and return its info in JSON format."""
        flights_info = {}
        
        if flight_id in self.data:
            for key in ['Number', 'DepartureTime', 'ArrivalTime']:
                flights_info[key] = self.data[flight_id].get(key)
        else:
            return None
            
        flights_info_json = json.dumps(flights_info)
        return flights_info_json
