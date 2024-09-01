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
        animal_infos = load_data(file_path)

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


def generate_new_string(dic):

    replace_parts = ""

    # generate strings from simple_infos
    for a_name, a_infos in dic.items():

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


def replace_template(json_file, template_file):
    with open(template_file, "r") as file:
        old_file = file.read()

    # file_path = "animals_data.json"
    dic = get_simple_infos(json_file)

    new_string = generate_new_string(dic)

    new_file = old_file.replace("__REPLACE_ANIMALS_INFO__", new_string)

    with open("animals.html", "w") as new_template:
        new_template.write(new_file)


# print(get_simple_infos("animals_data.json"))
replace_template("animals_data.json", "animals_template.html")



