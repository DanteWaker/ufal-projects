// ...importações e código anterior...

import axios from "axios";
import { useState } from "react";

const EditModal = ({ isOpen, onClose, pokemon, onEdit }) => {
  const [editedPokemon, setEditedPokemon] = useState(pokemon);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEditedPokemon({
      ...editedPokemon,
      [name]: value,
    });
  };

  const handleEditClick = () => {
    axios
      .put(`http://localhost:3000/api/pokemons/${editedPokemon.id}`, editedPokemon)
      .then(() => {
        onEdit(editedPokemon);
        onClose();
      })
      .catch((error) => {
        console.error("Erro ao editar Pokémon:", error);
      });
  };

  return (
    <div className={`fixed inset-0 flex items-center justify-center ${isOpen ? '' : 'hidden'}`}>
      <div className="bg-white p-4 rounded-md shadow-md">
        <h2 className="text-xl font-semibold mb-4">Editar Pokémon</h2>
        <div className="mb-4">
          <label className="block font-semibold mb-2">Nome:</label>
          <input
            type="text"
            name="name"
            value={editedPokemon.name}
            onChange={handleInputChange}
            className="w-full border rounded-md p-2"
          />
        </div>
        <div className="mb-4">
          <label className="block font-semibold mb-2">Descrição:</label>
          <textarea
            name="description"
            value={editedPokemon.description}
            onChange={handleInputChange}
            className="w-full border rounded-md p-2"
          />
        </div>
        <div className="mb-4">
          <label className="block font-semibold mb-2">Tipo:</label>
          <input
            type="text"
            name="types"
            value={editedPokemon.types}
            onChange={handleInputChange}
            className="w-full border rounded-md p-2"
          />
        </div>
        <div className="flex justify-end">
          <button
            className="bg-green-500 hover:bg-green-600 text-white py-2 px-4 rounded-full mr-2"
            onClick={handleEditClick}
          >
            Salvar
          </button>
          <button
            className="bg-gray-300 hover:bg-gray-400 text-gray-800 py-2 px-4 rounded-full"
            onClick={onClose}
          >
            Fechar
          </button>
        </div>
      </div>
    </div>
  );
};

export default EditModal;
