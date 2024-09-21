
from animals_web_generator import replace_template, get_infos_from_api, get_simple_infos, generate_new_string, get_user_input


def main():

    animal_name = get_user_input()

    replace_template(animal_name, "animals_template.html")


if __name__ == '__main__':
    main()