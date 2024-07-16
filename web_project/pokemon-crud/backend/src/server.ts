import "reflect-metadata";
import express from 'express';
import { AppDataSource } from '../ormconfig'; 
import pokemonRoutes from './routes/pokemonRoutes';
import cors from 'cors';

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(cors());

AppDataSource.initialize().then(() => {
    console.log('Conectado ao banco de dados com DataSource');

    // Rotas
    app.use('/api/pokemons', pokemonRoutes);

    app.listen(PORT, () => {
        console.log(`Servidor rodando na porta ${PORT}`);
    });
}).catch(error => console.log('Erro ao conectar com o banco de dados:', error));
