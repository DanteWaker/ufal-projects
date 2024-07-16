'use client'

import Navbar from '../components/Navbar';
import PokemonForm from '../components/PokemonForm'; // Ajuste o caminho de importação conforme necessário

const CreatePokemonPage = () => {
  return (
    <>
      <Navbar />
      <div className="container mx-auto p-4">

        <h2 className="text-2xl font-bold mb-4">Adicionar Novo Pokémon</h2>
        <PokemonForm />
      </div>
    </>
  );
};

export default CreatePokemonPage;
