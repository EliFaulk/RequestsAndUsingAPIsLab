import requests
import json

# Get pokedex number to search for
num = input("What number? ")
print("--------------------------------")


# Get request with pokedex number using PokeAPI
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}")
pokemon = response.json()


# Format and print Pokedex info
formatted_types = ", ".join(pokemon["types"][x]["type"]["name"].title() for x in range(len(pokemon["types"])))

print(f"""
POKEDEX ENTRY #{num}
--------------------------------
Name: {pokemon["name"].title()}
Types: {formatted_types}
Height: {pokemon["height"]/10} m
Weight: {pokemon["weight"]/10} kg
""")
