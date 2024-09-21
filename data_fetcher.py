import requests
import pprint
import json
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')
URL = "https://api.api-ninjas.com/v1/animals"
headers = {'X-Api-Key': API_KEY}


def fetch_data(animal_name):

    api_url = f"{URL}?name={animal_name}"
    response = requests.get(api_url, headers=headers)

    # Check the response status
    if response.status_code == 200:
        content_type = response.headers.get("Content-Type")

        # Check if the response is JSON
        if 'application/json' in content_type:
            try:
                parsed = response.json()
                if parsed:
                    return parsed
                else:
                    print(f"No data found for '{animal_name}'.")
                    return None
            except ValueError:
                # Handle the case where JSON parsing fails
                print(f"Could not decode the response for '{animal_name}', received non-JSON response.")
        else:
            print(f"Expected JSON but received {content_type}. Here is the response content:")
            print(response.text)  # Print raw response content
    else:
        print(f"Failed to retrieve information for '{animal_name}'. Status code: {response.status_code}")
        print(f"Response content: {response.text}")  # Print raw response content to help debugging

    return None  # Return None when no valid data is retrieved


# print(get_infos_from_api("abc"))
# dogs = fetch_data("dog")
# print(type(dogs))
# print(len(dogs))
# print(dogs[0])
# print(dogs[0].keys())
# print(json.dumps(dogs[0], indent=4))
# print(type(json.dumps(dogs[0])))
# pprint.pprint(dogs[0])


def get_simple_infos(animal_name):

    # create an empty simple infos dict
    simple_infos = {}

    # get all infos from api
    infos = fetch_data(animal_name)

    try:

        if infos:

            # loop through the infos
            for info in infos:

                # get name from info
                a_name = info.get("name", "Unknown Name")

                # get first location from locations if available
                a_locations = info.get("locations", [])
                a_location = a_locations[0] if a_locations else "Unknown Location"

                # get diet and type from characteristics if available
                a_characteristics = info.get("characteristics", {})
                a_diet = a_characteristics.get("diet", "Unknown Diet")
                a_type = a_characteristics.get("type", "Unknown Type")

                # add key value pairs into simple infos dict
                simple_infos[a_name] = {
                    "location": a_location,
                    "diet": a_diet,
                    "type": a_type
                }

            return simple_infos

        else:
            print(f"{animal_name} not found.")
            return None

    except KeyError as ke:
        print(f"KeyError occurred in get_simple_info: {ke}")
        return None  # Ensure a safe return on error
    except Exception as e:
        print(f"An error occurred in get_simple_info: {e}")
        return None  # Return None on any general exception


# print(len(get_simple_infos("dragon")))
