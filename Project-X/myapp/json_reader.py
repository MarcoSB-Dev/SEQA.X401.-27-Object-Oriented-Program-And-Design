import json

def read_json(file_path):
    """
    Reads a JSON file and returns the parsed data.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None