import requests
import json
planet_list = []

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName') # Because I've already called the dictionary, I don't have to put brackets when referencing a key using .get().
            mass = planet.get('mass', {}).get('massValue') # calling the key mass, accessing it's dictionary, then following up with another .get() for the massValue to have a cleaner output.
            orbit_period = planet.get('sideralOrbit') # Fixed the error
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
            planet_list.append({
                "name":name,
                "mass": mass,
                "orbit_period": orbit_period
            })
    return planet_list
   
fetch_planet_data()

def find_heaviest_planet(planets):
    planets = planet_list
    max = 0
    heaviest_planet_name = ""
    
    for planet in planets:
        if planet['mass'] > max:
            max = planet['mass']
            heaviest_planet_name = planet['name']
    
    return heaviest_planet_name, max

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")