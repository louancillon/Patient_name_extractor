# Patient_name_extractor
This project is a simple webserver, implemented using Flask web application, that extracts patient names from medical documents using the NameExtractor class.

## Installation
To install the required packages, run: pip install -r requirements.txt

## Run the app
To run the web application, use the following command: python run.py
This will start the Flask development server on http://127.0.0.1:5000/.
You can then send a POST request to the web server with a JSON object representing a medical document: curl -X POST http://127.0.0.1:5000/extract-names -H "Content-Type: application/json" -d '<jsonfile>'

### Workflow:
1. Client sends a POST request to /extract-names with the document JSON.
2. Server receives the request and extracts patient name.
3. Server sends back a JSON response with the extracted name.

## Test the app
To test the application, you can use the tests files in the tests directory. 
To run the tests, use the following command: python3 -m unittest tests

## Project Structure

The project has the following structure:
Patient_name_extractor/
│
├── app/
│   ├── __init__.py
│   └── routes.py
│   └── text_processing/
│       └── __init__.py
│       └── name_extractor.py
│
├── tests/
│   ├── test_name_extractor.py
│   └── test_routes.py
│
├── data/
│   ├── consult.json
│   └── ...
│
├── requirements.txt
├── README.md
└── run.py

app/: Contains the Flask application code.
    name_extractor.py: Defines the NameExtractor class, which is used to extract patient names from medical documents.
    routes.py: Defines the Flask routes for the web application.
tests/: Contains the unit tests for the application.
    test_routes.py: Defines the unit tests for the Flask routes.
    test_name_extractor.py: Defines the unit tests for the NameExtractor class.
data/: Contains the json files corresponding to the input medical documents.

requirements.txt: Lists the required packages for the application.
README.md: This file.
run.py: Starts the Flask development server.


## TODO/Improvements : 
The NameExtractor class and extract_patient function are very simple and could be improved : 
1. Handle more complex names: If there are middle names, if the names are misspelled, or if the uppercase is missing, the function should still be able to extract the patient's name accurately.
2. Use a more robust indicator word list: By observing many documents, we can identify the most frequent words associated with the patient names and use them to improve the indicator word list.
3. Incorporate contextual/spatial information: 
    1. Recognize the type of medical document and adapt the extraction method accordingly. 
    2. Use the layout to detect if the word is in the header, footer, or other specific locations in the document.
4. Consistent name format: The function could be improved by returning the name of the patient in a consistent format, such as "Firstname Surname" or "Firstname SURNAME".
5. Better handle errors and edge cases: The function could be improved by adding error handling and edge case detection to provide more informative feedback to the user.
6. Improve efficiency: The function could be improved by using more efficient search algorithms or by incorporating other techniques to reduce the search space.
