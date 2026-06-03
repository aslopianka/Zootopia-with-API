import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
ANIMALS_API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  query_params = {'name': animal_name}
  api_headers = {"X-Api-Key": API_KEY}

  res = requests.get(ANIMALS_API_URL, params=query_params, headers=api_headers)
  if res.status_code == 200:
      return res.json()
  return []