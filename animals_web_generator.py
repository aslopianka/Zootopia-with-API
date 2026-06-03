import json
import requests

ANIMALS_API_URL = "https://api.api-ninjas.com/v1/animals?name=fox"
API_KEY = "UvCmNExEFbxvWgBcykOGTOMmMdkSWHgrCJaLbBLM"


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def fetch_animal_data():
    res = requests.get(ANIMALS_API_URL, headers={"X-Api-Key": API_KEY})
    return res.json()


def serialize_animal(animals_data):

    output_string = ""
    for animal in animals_data:
        char = animal.get('characteristics', {})
        tax = animal.get('taxonomy', {})
        name = animal.get('name', '-')

        details = {
            "Scientific Name": tax.get('scientific_name'),
            "Diet": char.get('diet'),
            "Location": animal.get('locations', [None])[0],
            "Type": char.get('type')
        }

        list_items = ""
        for label, value in details.items():
            if value:
                list_items += f"<li><strong>{label}:</strong> {value}</li>\n"

        output_string += f"""
                <li class="cards__item">
                  <div class="card__title">{name}</div>
                  <div class="card__text">
                    <ul class="card__list">
                      {list_items}
                    </ul>
                  </div>
                </li>
                """

    return output_string

def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_html_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def main():

    animal_data = fetch_animal_data()
    output_string = serialize_animal(animal_data)
    html_content = read_html_file('animals_template.html')
    html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output_string)
    write_html_file('animals.html', html_content)


if __name__ == "__main__":
    main()