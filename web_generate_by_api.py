import requests
import pprint
import json

# Ensure the URL and API key are correct according to the API's documentation
URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "i8L6sOVnB7TS5a4pI2jfxg==fK8WQsRazLbNNDw1"  # Double-check your key here
headers = {'X-Api-Key': API_KEY}


def get_json_from_api(name):

    api_url = f"{URL}?name={name}"  # Ensure proper query parameter syntax
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
                    print(f"No data found for '{name}'.")
                    return None
            except ValueError:
                # Handle the case where JSON parsing fails
                print(f"Could not decode the response for '{name}', received non-JSON response.")
        else:
            print(f"Expected JSON but received {content_type}. Here is the response content:")
            print(response.text)  # Print raw response content
    else:
        print(f"Failed to retrieve information for '{name}'. Status code: {response.status_code}")
        print(f"Response content: {response.text}")  # Print raw response content to help debugging

    return None  # Return None when no valid data is retrieved


# print(get_json_from_api("abc"))
# dogs = get_json_from_api("dog")
# print(type(dogs))
# print(len(dogs))
# print(dogs[0])
# print(dogs[0].keys())
# print(json.dumps(dogs[0], indent=4))
# print(type(json.dumps(dogs[0])))
# pprint.pprint(dogs[0])
