import React from 'react';
import { Link } from 'react-router-dom';

function NotFound() {
  return (
    <div className="container center">
      <h1>404 - Página não encontrada</h1>
      <p>A página que você procura não existe.</p>
      <Link to="/">Voltar para home</Link>
    </div>
  );
}

export default NotFound;
