'use client'

import Link from 'next/link';

const Navbar = () => {
  return (
    <nav className="bg-gray-800 text-white p-4">
      <div className="container mx-auto flex justify-between">
        <Link href="/">
          <div className="text-lg font-bold">Pokémon App</div>
        </Link>
        <div>
          <Link href="/create">
            <div className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Add Pokémon
            </div>
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
