import json


def load_data(file_path):
    """ Loads a JSON file """
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: file {file_path} was not found.")
    except json.JSONDecodeError:
        print("Error: failed to decode json.")
        return []


def get_simple_infos(file_path):

    try:

        # load json data
        animal_infos = load_data("animals_data.json")

        # debug code
        animal_names = list(map(lambda animal: animal["name"], animal_infos))
        print(f"There are totally {len(animal_names)} animals in original.")

        # set a empty dic
        simple_infos = {}

        # loop through animal infos and return simple infos
        for animal_info in animal_infos:

            name = animal_info.get("name", None)
            characteristics = animal_info.get("characteristics", None)
            diet = characteristics.get("diet", "None") if characteristics else None
            locations = animal_info.get("locations", None)
            location = locations[0] if locations else None
            a_type = characteristics.get("type", None) if characteristics else None

            simple_infos[name] = {
                "diet": diet,
                "location": location,
                "type": a_type
            }

        # debug code
        print(f"There are totally {len(animal_infos)} animals in simple infos.")

        return simple_infos
    except Exception as e:
        print(f"An error occurred in get_simple_infos: {e}")


def print_simple_infos(dic):
    try:
        for a_name, a_infos in dic.items():

            print()
            if a_name:
                print(f"Name: {a_name}")
            if a_infos:
                diet = a_infos["diet"]
                if diet:
                    print(f"Diet: {diet}")
                location = a_infos["location"]
                if location:
                    print(f"Location: {location}")
                a_type = a_infos["type"]
                if a_type:
                    print(f"Type: {a_type}")
                print()

    except Exception as e:
        print(f"An error occurred in print_simple_infos: {e}")

# dic = get_simple_infos("animals_data.json")
# print_simple_infos(dic)



