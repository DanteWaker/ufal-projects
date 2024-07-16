'use client'
import React, { useEffect, useState } from 'react';
import Navbar from './components/Navbar';
import axios from 'axios';
import PokemonItem from './components/PokemonItem';

const Index = () => {
  const [pokemons, setPokemons] = useState([]);

  useEffect(() => {
    axios({
      method: 'get',
      url: 'http://localhost:3000/api/pokemons',
      responseType: 'stream'
    }).then((response) => response.data) // Obtenha os dados da resposta
      .then((data) => JSON.parse(data)) // Analise os dados JSON
      .then((parsedData) => setPokemons(parsedData));
  }, []);

  const handleDelete = () => {
    axios.get('http://localhost:3000/api/pokemons')
      .then((response) => {
        setPokemons(response.data);
      })
      .catch((error) => {
        console.error("Erro ao carregar a lista de Pokémon após a exclusão:", error);
      });
  };
  const onEdit = () => {
    axios.get('http://localhost:3000/api/pokemons')
      .then((response) => {
        setPokemons(response.data);
      })
      .catch((error) => {
        console.error("Erro ao carregar a lista de Pokémon após a exclusão:", error);
      });
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <main className="container mx-auto py-8">
        <h1 className="text-2xl font-bold text-center text-gray-800">Bem-vindo ao App Pokémon</h1>
        <div className="mt-8">
          {pokemons.map((pokemon) => (
            <PokemonItem key={pokemon.id} pokemon={pokemon} onDelete={handleDelete} onEdit={onEdit} />
          ))}
        </div>
      </main>
    </div>
  );
};

export default Index;
