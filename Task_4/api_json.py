import requests
import csv
import json
url = "https://api.restful-api.dev/objects"
import requests
import json
from pathlib import Path

def fetch_and_save_json(api_url: str, output_filepath: str, headers: dict = None) -> None:
    """
    Fetches JSON data from a given API endpoint and saves it to a local file.
    
    Args:
        api_url (str): The URL of the API endpoint.
        output_filepath (str or Path): The local path where the JSON file will be saved.
        headers (dict, optional): Optional headers for the request (e.g., Authorization tokens).
    """
    try:
        # 1. Send GET request to the API
        response = requests.get(api_url, headers=headers, timeout=10)
        
        # Raise an exception for HTTP error codes (4xx or 5xx)
        response.raise_for_status()
        
        # 2. Parse the response content as JSON
        data = response.json()
        
        # 3. Ensure the target directory exists
        path = Path(output_filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # 4. Write the JSON data to the local file
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print(f"Successfully saved API data to: {path.resolve()}")
        
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
    except json.JSONDecodeError:
        print("Error: The API response was not valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
fetch_and_save_json(url,'data_output\\new_data.json')