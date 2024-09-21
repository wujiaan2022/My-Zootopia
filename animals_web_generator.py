from data_fetcher import fetch_data


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



