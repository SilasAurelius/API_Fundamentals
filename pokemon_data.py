import requests

# I used the api without the pikachu part so it's more versatile in calling other pokemon data.
api_get = "https://pokeapi.co/api/v2/"

def fetch_pokemon_data(pokemon_name):
    url = f"{api_get}/pokemon/{pokemon_name}"
    response = requests.get(url)
    # I wrote an if statement to check the api status. If 200, good to go!
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {pokemon_name}")
        return None

def convert_hectograms_to_pounds(hectograms):
    return hectograms * 0.220462
    # The pokemon api uses hectograms for weight. I had no idea what a hectogram is so I found out and converted it to pounds.
    
    
def print_pokemon_abilities(pokemon_data):
    # I wanted the ability list to output in an easier format to read to I used a for loop to iterate over each one.
    if 'abilities' in pokemon_data:
        print(f"Abilities:")
        for ability in pokemon_data['abilities']:
            ability_name = ability['ability']['name'].title()
            print(f"# {ability_name}")
    else:
        print("No abilities data available.")    

def calculate_average_weight(pokemon_list):
    total_weight_in_pounds = 0
    count = 0
    
    for pokemon_name in pokemon_list:
        pokemon_data = fetch_pokemon_data(pokemon_name)
        if pokemon_data:
            weight_in_hectograms = pokemon_data['weight']
            weight_in_pounds = convert_hectograms_to_pounds(weight_in_hectograms)
            total_weight_in_pounds += weight_in_pounds
            count += 1
    
        print(f"\n{pokemon_name.capitalize()}'s Abilities:")
        print_pokemon_abilities(pokemon_data)
        
    if count > 0:
        average_weight_in_pounds = total_weight_in_pounds / count
        return average_weight_in_pounds
    else:
        return None

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
average_weight_in_pounds = calculate_average_weight(pokemon_names)
print(f"The average weight of this Pokemon team in pounds is: {average_weight_in_pounds:.2f} lbs")