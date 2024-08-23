from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time

async def get_ability(client, url):
    start_time = time.perf_counter()
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    ability = resp.json()
    end_time = time.perf_counter()
    print(f"Time taken for {url}: {end_time-start_time:.2f} seconds")
    return ability

async def get_abilities():
    async with httpx.AsyncClient() as client:
        battle_armor_url = "https://pokeapi.co/api/v2/ability/battle-armor"
        speed_boost_url = "https://pokeapi.co/api/v2/ability/speed-boost"

        tasks = [
            get_ability(client, battle_armor_url),
            get_ability(client, speed_boost_url)
        ]

        abilities = await asyncio.gather(*tasks)
        return abilities

async def index():
    start_time = time.perf_counter()
    abilities = await get_abilities()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get abilities. Time taken:{end_time-start_time:.2f} seconds")

    for ability in abilities:
        print(f"Ability: {ability['name']}")
        print(f"Number of Pokémon with this ability: {len(ability['pokemon'])}")
        print("Pokémon with this ability:")
        for pokemon in ability['pokemon']:
            print(pokemon['pokemon']['name'])
        print()

if __name__ == '__main__':
    asyncio.run(index())