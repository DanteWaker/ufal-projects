import { DataSource } from 'typeorm';
import { Pokemon } from './src/entities/Pokemon';

export const AppDataSource = new DataSource({
    type: "sqlite",
    database: "./data/pokemonDB.sqlite",
    synchronize: true,
    logging: false,
    entities: [Pokemon],
    migrations: [],
    subscribers: [],
})
