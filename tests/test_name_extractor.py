import unittest
import os
import json
from flask import json
from app import create_app
from parameterized import parameterized
from app.text_processing import NameExtractor

class ExtractNamesTestCase(unittest.TestCase):
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
            {"first_name": "Jean", "last_name": "DUPONT"}
        ),
        (
            "valid_document2",
            "compte_rendu_operation.json",  
            {"first_name": None, "last_name": "Hugo"}
        ),
        (
            "valid_document3",
            "rdv_confirmation.json",  
            {"first_name": "Juliette", "last_name": "MARTIN"}
        ),
        (
            "names_not_found",
            "noname.json", 
            None
        )
    ])
    def test_extract_names(self, name, filename, expected_response):
        med_text = self.load_json_from_file(filename)
        name_extractor = NameExtractor()
        words = name_extractor.flatten_and_sort_words(med_text)
        patient_name = name_extractor.extract_patient(words)
        self.assertEqual(patient_name, expected_response)

    @parameterized.expand([
        (
            "short_text",
            "short_text.json",  
            [{'text': 'Hello', 'bbox': {'x_min': 0.12, 'x_max': 0.19, 'y_min': 0.09, 'y_max': 0.1}}, {'text': ',', 'bbox': {'x_min': 0.19, 'x_max': 0.21, 'y_min': 0.09, 'y_max': 0.1}}, {'text': 'This', 'bbox': {'x_min': 0.21, 'x_max': 0.28, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'is', 'bbox': {'x_min': 0.28, 'x_max': 0.31, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'a', 'bbox': {'x_min': 0.31, 'x_max': 0.33, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'test', 'bbox': {'x_min': 0.33, 'x_max': 0.38, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'to', 'bbox': {'x_min': 0.38, 'x_max': 0.41, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'see', 'bbox': {'x_min': 0.41, 'x_max': 0.45, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'if', 'bbox': {'x_min': 0.45, 'x_max': 0.47, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'the', 'bbox': {'x_min': 0.47, 'x_max': 0.5, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'function', 'bbox': {'x_min': 0.5, 'x_max': 0.57, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'is', 'bbox': {'x_min': 0.57, 'x_max': 0.6, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'working', 'bbox': {'x_min': 0.6, 'x_max': 0.67, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'well', 'bbox': {'x_min': 0.67, 'x_max': 0.71, 'y_min': 0.12, 'y_max': 0.1}}, {'text': '.', 'bbox': {'x_min': 0.71, 'x_max': 0.73, 'y_min': 0.12, 'y_max': 0.1}}, {'text': 'Best', 'bbox': {'x_min': 0.12, 'x_max': 0.19, 'y_min': 0.16, 'y_max': 0.17}}, {'text': ',', 'bbox': {'x_min': 0.19, 'x_max': 0.21, 'y_min': 0.16, 'y_max': 0.17}}, {'text': 'Testteam', 'bbox': {'x_min': 0.21, 'x_max': 0.33, 'y_min': 0.16, 'y_max': 0.17}}]
        ),
        
    ])
    def test_flatten_and_sort_words(self, name, filename, expected_output):
        text = self.load_json_from_file(filename)
        name_extractor = NameExtractor()
        out = name_extractor.flatten_and_sort_words(text)
        self.assertEqual(out, expected_output)

if __name__ == "__main__":
    unittest.main()

