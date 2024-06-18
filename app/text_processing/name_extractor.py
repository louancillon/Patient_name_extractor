class NameExtractor:
    """
    A class for extracting the name of a patient from a medical document in JSON format.
    """
    def __init__(self):
        # List of indicator words that signal the start of a patient's name
        self.indicator_words = ["Monsieur", "Madame", "Mr.", "Ms.", "Mme.", "Patient", "Patiente"]
        
    def extract_patient(self, med_text):
        """
        Function to extract the name of the patient from a list of dictionaries representing a medical text.

        Args:
            med_text (list of dict): List of dictionaries representing a medical text, where each dictionary contains information about a word in the text. Each dictionary has the following format:
                {"text": "<word text>", "bbox": {"x_min": <x coordinate of left side of bounding box>,
                                                "x_max": <x coordinate of right side of bounding box>,
                                                "y_min": <y coordinate of bottom of bounding box>,
                                                "y_max": <y coordinate of top of bounding box>}}
            The list is already sorted in the order of reading.

        Returns:
            dict: A JSON object containing the first and last name of the patient, or an error message if no name is found. The JSON object has the following format:
                {"first_name": "<first name>", "last_name": "<last name>"}
                or
                {"error": "Names not found"}
        """
        # Iterate over each word in the medical text
        i = 0
        while i < len(med_text):
            # Check if the current word is an indicator word
            if med_text[i]['text'] in self.indicator_words:
                potential_names = []
                for j in range(1, 4):
                    # Check if the following word is a potential name
                    if i + j < len(med_text) and med_text[i + j]['text'][0].isupper():
                        potential_names.append(med_text[i + j]['text'])
                    else:
                        break

                if len(potential_names) == 2: # If there is one first name and one last name, ex: Mme Lucie Dupont
                    first_name = potential_names[0]
                    last_name = potential_names[1]
                    #return jsonify({"first_name": first_name, "last_name": last_name})
                    return {"first_name": first_name, "last_name": last_name}
                elif len(potential_names) == 1: # If the first name is not specified, ex: Mme Dupont
                    last_name = potential_names[0]
                    #return jsonify({"first_name": None, "last_name": last_name})
                    return {"first_name": None, "last_name": last_name}
                elif len(potential_names) == 3: # If there are two last names or a composed last name, ex : Mme Lucie Dupont Martin
                    first_name = potential_names[0]
                    last_name = potential_names[1] + " " + potential_names[2]
                    #return jsonify({"first_name": first_name, "last_name": last_name})
                    return {"first_name": first_name, "last_name": last_name}
                else:
                    i += 1  
            else:
                i += 1  

        # If no name has been found 
        return None
        #return jsonify({"error": "Names not found"}), 404

    def flatten_and_sort_words(self, data):
        """
        Function that takes a JSON object representing a medical document, where each word is represented as a dictionary with the following format:
            {"text": "<word text>", "bbox": {"x_min": <x coordinate of left side of bounding box>,
                                            "x_max": <x coordinate of right side of bounding box>,
                                            "y_min": <y coordinate of bottom of bounding box>,
                                            "y_max": <y coordinate of top of bounding box>}}
        The function extracts all words from the document and sorts them in reading order based on their bounding box coordinates (y_min first, then x_min).
        Returns a list of dictionaries representing each word in the sorted order.
        """
        # Extract all words from the data and store them in a list
        words = []
        for page in data['pages']:
            for word in page['words']:
                words.append(word)

        # Sort words by y_min first, then x_min to have the text in the good order 
        words.sort(key=lambda w: (w['bbox']['y_min'], w['bbox']['x_min']))
        return words
