# Zootopia-with-API

## Project Description
`Zootopia-with-API` is a Python project that lets users search for animals and automatically generates an HTML page with animal cards based on live API data.

It solves the problem of manually collecting and formatting animal information by fetching details (like scientific name, diet, location, and type) from the API and injecting them into a ready-made HTML template.


## Usage
1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API key**
   Create a `.env` file in the project root and add:
   ```env
   API_KEY=your_api_ninjas_api_key_here
   ```

3. **Run the generator**
   ```bash
   python animals_web_generator.py
   ```

4. **Enter an animal name** when prompted (for example: `lion`, `fox`, `koala`).

5. **Open the output file**
   After running, the script creates/updates `animals.html`. Open it in your browser to view the generated animal cards.

### Notes
- If no matching animal is found, the generated page will show a friendly “doesn't exist” message.
- Make sure your API key is valid; otherwise, the API request will return no data.