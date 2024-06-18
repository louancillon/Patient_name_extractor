import unittest
import os
import json
from flask import json
from app import create_app
from parameterized import parameterized

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        """
        Initialize app and test environment
        """
        self.app = create_app()
        self.client = self.app.test_client
        self.headers = {'Content-Type': 'application/json'}

    def load_json_from_file(self, filename):
        """
        Helper function to load JSON data from file.
        """
        file_path = os.path.join("/Users/louancillon/Desktop/lien_assignment/data/", filename)
        with open(file_path, 'r') as f:
            return json.load(f)

    @parameterized.expand([
        (
            "valid_document1",
            "consult.json",  
            200, # 200 OK : The request was successful and the server returned the expected response.
            {"first_name": "Jean", "last_name": "DUPONT"}
        ),
        (
            "valid_document2",
            "compte_rendu_operation.json",  
            200,
            {"first_name": None, "last_name": "Hugo"}
        ),
        (
            "valid_document3",
            "rdv_confirmation.json",  
            200,
            {"first_name": "Juliette", "last_name": "MARTIN"}
        ),
        (
            "missing_data",
            "missing_data.json", 
            400, #400 Bad Request: The request was invalid or malformed. 
            {"error": "Invalid input"}
        ),
        (
            "names_not_found",
            "noname.json", 
            404, #404 Not Found: The requested resource was not found on the server.
            {"error": "Names not found"}
        )
    ])
    def test_extract_names(self, name, filename, expected_status, expected_response):
        payload = self.load_json_from_file(filename)
        response = self.client().post('/extract-names', headers=self.headers, data=json.dumps(payload))
        data = json.loads(response.data)
        self.assertEqual(response.status_code, expected_status)
        self.assertEqual(data, expected_response)

    
if __name__ == "__main__":
    unittest.main()

