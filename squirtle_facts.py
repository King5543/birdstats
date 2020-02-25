import json

if __name__ == '__main__':
    with open("squirtle.json", 'r') as f:
        squirtle_facts = json.load(f)
        print(json.dumps(squirtle_facts['stats']['base stat']['name']))
    for ability in squirtle_facts['abilities']:
        print(ability['ability']['name'])
    for move_dict in squirtle_facts['moves']:
        print(move_dict['move']['name'], 'is an ability!')
    print('Loaded!')
