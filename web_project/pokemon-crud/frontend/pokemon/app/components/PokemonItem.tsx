import React, { useState } from 'react';
import axios from 'axios';
import { FaTrash, FaEdit } from 'react-icons/fa';
import EditModal from './EditModal';

// ...importações e código anterior...

const PokemonItem = ({ pokemon, onDelete, onEdit }) => {
  const [isEditModalOpen, setEditModalOpen] = useState(false);

  const handleDeleteClick = () => {
    axios
      .delete(`http://localhost:3000/api/pokemons/${pokemon.id}`)
      .then(() => {
        onDelete();
      })
      .catch((error) => {
        console.error("Erro ao excluir Pokémon:", error);
      });
  };

  const handleEditClick = () => {
    setEditModalOpen(true);
  };

  return (
    <div className="bg-white p-4 rounded-md shadow-md mb-4 flex justify-between items-center">
      <div>
        <p className="font-semibold">Nome: {pokemon.name}</p>
        <p className="text-gray-600">Descrição: {pokemon.description}</p>
        <p className="text-gray-600">Tipo: {pokemon.types}</p>
      </div>
      <div className="flex items-center space-x-4">
        <button
          className="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-full"
          onClick={handleEditClick}
        >
          <FaEdit className="mr-1" /> Editar
        </button>
        <button
          className="bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded-full"
          onClick={handleDeleteClick}
        >
          <FaTrash className="mr-1" /> Excluir
        </button>
      </div>
      <EditModal
        isOpen={isEditModalOpen}
        onClose={() => setEditModalOpen(false)}
        pokemon={pokemon}
        onEdit={() => {
          onEdit();
          setEditModalOpen(false);
        }}
      />
    </div>
  );
};

export default PokemonItem;
