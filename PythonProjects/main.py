import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd9fab4d3cd3c1a206ec78c1020358e11'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "qoqfh@starmail.net",
    "password": "PythonoNancyCODING1"
}
body_confirmation = {
    "trainer_token" : TOKEN
}
body_create = {
    "name": "Snakie",
    "photo_id": 73
}
body_change = {
    "pokemon_id": "72920",
    "name": "PythoSnakie",
    "photo_id": 183
}
body_pokemon = {
    "pokemon_id": "72920"
}

# response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
# print(response.text)

# response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
# print(response_confirmation.text)

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

# response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
# print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon)
print(response_pokeball.text)