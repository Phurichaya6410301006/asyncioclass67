import aiofiles
import asyncio
import json

pokemonapi_directory = 'C:/Users/HP/Desktop/asyncioclass67/assignment07/pokemon/pokemonapi'
pokemonmove_directory = 'C:/Users/HP/Desktop/asyncioclass67/assignment07/pokemon/pokemonmove'

async def main():
    # Read the contents of the json file.
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode='r') as f:
        contents = await f.read()
    print(contents)

asyncio.run(main())