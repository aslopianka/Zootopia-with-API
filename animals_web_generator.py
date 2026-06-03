import json
import data_fetcher


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


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
    animal_search_term = input("Enter the animal you would like to search: ")
    animal_data = data_fetcher.fetch_data(animal_search_term)
    if not animal_data:
        output_string = f"""
            <div style="text-align: center; margin: 40px auto; max-width: 500px;">
              <h2>The animal "{animal_search_term}" doesn't exist.</h2>
              <p style="color: #666; font-size: 1.1rem;">Please try a different animal or check your spelling.</p>
            </div>
            """
    else: output_string = serialize_animal(animal_data)
    html_content = read_html_file('animals_template.html')
    html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output_string)
    write_html_file('animals.html', html_content)


if __name__ == "__main__":
    main()