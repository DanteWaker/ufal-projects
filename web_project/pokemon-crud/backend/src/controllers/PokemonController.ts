import { Request, Response } from 'express';
import { Pokemon } from '../entities/Pokemon';
import { AppDataSource } from '../../ormconfig';

export const getPokemons = async (req: Request, res: Response) => {
  const pokemonRepository = AppDataSource.getRepository(Pokemon);
  const pokemons = await pokemonRepository.find();
  res.json(pokemons);
};

export const createPokemon = async (req: Request, res: Response) => {
    const pokemonRepository = AppDataSource.getRepository(Pokemon); 
    const { name, description, image, types } = req.body;

    const pokemon = pokemonRepository.create({
        name,
        description,
        image,
        types,
    });

    await pokemonRepository.save(pokemon);

    return res.json(pokemon);
};

export const updatePokemon = async (req: Request, res: Response) => {
  const { id } = req.params;
  const { name, description, image, types } = req.body;

  const pokemonRepository = AppDataSource.getRepository(Pokemon);
  let pokemon = await pokemonRepository.findOneBy({ id: parseInt(id) });

  if (pokemon) {
      pokemon.name = name;
      pokemon.description = description;
      pokemon.image = image;
      pokemon.types = types;
      await pokemonRepository.save(pokemon);
      return res.json(pokemon);
  } else {
      return res.status(404).json({ message: "Pokémon não encontrado" });
  }
};

export const deletePokemon = async (req: Request, res: Response) => {
  const { id } = req.params;

  const pokemonRepository = AppDataSource.getRepository(Pokemon);
  let pokemon = await pokemonRepository.findOneBy({ id: parseInt(id) });

  if (pokemon) {
      await pokemonRepository.remove(pokemon);
      return res.status(204).send();
  } else {
      return res.status(404).json({ message: "Pokémon não encontrado" });
  }
};
