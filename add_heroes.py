import json
import csv


with open('SuperHero.json', 'r') as json_file:
    data = json.load(json_file)


new_heroes = [
    {
        "name": "Captain America",
        "age": 35,
        "secretIdentity": "Steve Rogers",
        "powers": ["Superhuman strength", "Shield throwing"]
    },
    {
        "name": "Spider-Man",
        "age": 22,
        "secretIdentity": "Peter Parker",
        "powers": ["Wall-crawling", "Web-slinging"]
    }
]

data['members'].extend(new_heroes)


with open('SuperHero_updated.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

print("Новые герои успешно добавлены в JSON файл с обновленными данными.")
