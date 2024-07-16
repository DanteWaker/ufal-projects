'use client'

import axios from 'axios';
import React, { useState } from 'react';

const PokemonForm = () => {
  const [pokemon, setPokemon] = useState({
    name: '',
    description: '',
    image: '',
    types: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setPokemon({ ...pokemon, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log({
        name: pokemon.name,
        description: pokemon.description,
        image: pokemon.image,
        types: pokemon.types.split(',').map(type => type.trim()),
      })
      const response = await axios.post('http://localhost:3000/api/pokemons', {
        name: pokemon.name,
        description: pokemon.description,
        image: pokemon.image,
        types: pokemon.types.split(',').map(type => type.trim()),
      });

      console.log(response.data);
      setPokemon({ name: '', description: '', image: '', types: '' });
    } catch (error) {
      console.error("Erro ao criar Pokémon:", error);
    }
  };


  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="name" className="block text-sm font-medium text-gray-700">Nome</label>
        <input type="text" name="name" id="name" required
          className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          value={pokemon.name} onChange={handleChange} />
      </div>
      <div>
        <label htmlFor="description" className="block text-sm font-medium text-gray-700">Descrição</label>
        <textarea name="description" id="description" required
          className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          value={pokemon.description} onChange={handleChange}></textarea>
      </div>
      <div>
        <label htmlFor="image" className="block text-sm font-medium text-gray-700">Imagem URL</label>
        <input type="text" name="image" id="image"
          className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          value={pokemon.image} onChange={handleChange} />
      </div>
      <div>
        <label htmlFor="types" className="block text-sm font-medium text-gray-700">Tipo(s)</label>
        <input type="text" name="types" id="types"
          className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          value={pokemon.types} onChange={handleChange} placeholder="Ex: fogo, água" />
      </div>
      <div>
        <button type="submit" className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Criar Pokémon
        </button>
      </div>
    </form>
  );
};

export default PokemonForm;
