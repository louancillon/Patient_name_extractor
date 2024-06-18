from flask import Blueprint, request, jsonify
from app.text_processing import NameExtractor

# Create a Flask blueprint for the main module
main = Blueprint('main', __name__)

@main.route('/extract-names', methods=['POST'])
def extract_names():
    """
    Function to extract the name of the patient from a medical document in JSON format.
    This function is a Flask route that accepts POST requests to the '/extract-names' endpoint. 
    It expects a JSON object containing a medical document as input and returns the extracted name as a JSON object.
    """
    # Get the JSON data from the request
    med_doc = request.get_json()

    if not med_doc: # Check if the data is valid
        return jsonify({"error": "Invalid input"}), 400

    name_extractor = NameExtractor()
    words = name_extractor.flatten_and_sort_words(med_doc) # Use the NameExtractor to obtain the records in the reading order 
    patient_name = name_extractor.extract_patient(words)
    
    # Return the extracted name as a JSON object
    if patient_name:
        return jsonify(patient_name)
    return jsonify({"error": "Names not found"}), 404

    
