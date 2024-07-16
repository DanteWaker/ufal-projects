import { Router } from 'express';
import { getPokemons, createPokemon, updatePokemon, deletePokemon } from '../controllers/PokemonController';

const router = Router();

router.get('/', getPokemons);
router.post('/', createPokemon);
router.put('/:id', updatePokemon);
router.delete('/:id', deletePokemon);

export default router;
