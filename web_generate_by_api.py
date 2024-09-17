import requests
import pprint
import json

# Ensure the URL and API key are correct according to the API's documentation
URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "i8L6sOVnB7TS5a4pI2jfxg==fK8WQsRazLbNNDw1"  # Double-check your key here
headers = {'X-Api-Key': API_KEY}


def get_infos_from_api(name):

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


# print(get_infos_from_api("abc"))
# dogs = get_infos_from_api("dog")
# print(type(dogs))
# print(len(dogs))
# print(dogs[0])
# print(dogs[0].keys())
# print(json.dumps(dogs[0], indent=4))
# print(type(json.dumps(dogs[0])))
# pprint.pprint(dogs[0])

def get_simple_infos(name):

    # create an empty simple infos dict
    simple_infos = {}

    # get all infos from api
    infos = get_infos_from_api(name)

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
            print(f"{name} not found.")
            return None

    except KeyError as ke:
        print(f"KeyError occurred in get_simple_info: {ke}")
        return None  # Ensure a safe return on error
    except Exception as e:
        print(f"An error occurred in get_simple_info: {e}")
        return None  # Return None on any general exception


# print(len(get_simple_infos("dragon")))


def generate_new_string(name):

    simple_infos = get_simple_infos(name)

    replace_parts = ""

    # generate strings from simple_infos
    for a_name, a_infos in simple_infos.items():

        replace_parts += '<li class="cards__item">'

        if a_name:

            replace_parts += f"<div class='card__title'>{a_name}</div><br/>"

            replace_parts += '<p class ="card__text">'

            if a_infos:
                diet = a_infos.get("diet")
                if diet:
                    replace_parts += f"<strong>Diet:</strong> {diet}<br/>"

                location = a_infos.get("location")
                if location:
                    replace_parts += f"<strong>Location:</strong> {location}<br/>"

                a_type = a_infos.get("type")
                if a_type:
                    replace_parts += f"<strong>Type:</strong> {a_type}<br/>"

                replace_parts += "</p>"
                replace_parts += "</li>"

    return replace_parts


# print(generate_new_string("dragon"))


def replace_template(animal_name, template_file):
    # Read the template file
    with open(template_file, "r") as file:
        old_file = file.read()

    # Fetch the new string with the animal name from API
    new_string = generate_new_string(animal_name)

    # Replace the placeholder in the template with the new string
    new_file = old_file.replace("__REPLACE_ANIMALS_INFO__", new_string)

    # Write the new file with the replaced content
    with open("animals.html", "w") as new_template:
        new_template.write(new_file)


# replace_template("dragon", "animals_template.html")

def get_user_input():
    while True:
        try:
            # Get the user input and strip leading/trailing spaces
            name = input("Please enter a name of an animal: ").strip().lower()

            # Remove all spaces in the input
            name_without_spaces = name.replace(" ", "")

            # Check if the input without spaces contains only alphabets
            if name_without_spaces.isalpha():
                return name_without_spaces
            else:
                print("Invalid input. Please enter a valid animal name containing only letters.")

        except Exception as e:
            print(f"An error occurred in user_input: {e}")
            return None



