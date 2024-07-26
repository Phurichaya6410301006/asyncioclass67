import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = 'C:/Users/HP/Desktop/asyncioclass67/assignment07/pokemon/pokemonapi'
pokemonmove_directory = 'C:/Users/HP/Desktop/asyncioclass67/assignment07/pokemon/pokemonmove'

async def main():
    pathlist = list(Path(pokemonapi_directory).glob('*.json'))[:150]
    
    for path in pathlist:
         # Read the contents of the json file.
        async with aiofiles.open(path, mode='r') as f:
            contents = await f.read()

        # Load it into a dictionary and create a list of moves.
        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]

        move_file_path = f'{pokemonmove_directory}/{name}_moves.txt'
         # Open a new file to write the list of moves into.
        async with aiofiles.open(move_file_path, mode='w') as f:
            await f.write('\n'.join(moves))
        
        print(f"Moves written to: {move_file_path}")

asyncio.run(main())