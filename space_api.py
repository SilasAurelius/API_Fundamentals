import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    planet_list = []
    
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
    max_mass = 0 # Changed variable name from mass to max_mass
    heaviest_planet_name = ""
    
    for planet in planets:
        mass = planet.get('mass')
        if mass is not None:
            if max_mass is None or mass > max_mass:
                max_mass = mass
                heaviest_planet_name = planet['name']
    
    return heaviest_planet_name, max_mass

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")