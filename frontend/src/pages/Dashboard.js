import React from 'react';

function Dashboard() {
  return (
    <div className="container">
      <h1>🍕 Dashboard - Sistema de Gestão de Pizzaria</h1>
      <p>Bem-vindo ao TRONIX!</p>
      <div className="grid">
        <div className="card">
          <h2>🤖 Robô do Caixa</h2>
          <p>Pagamento com PIX e Cartão</p>
        </div>
        <div className="card">
          <h2>🧑‍💼 Garçom</h2>
          <p>Lançar pedidos</p>
        </div>
        <div className="card">
          <h2>👨‍🍳 Cozinha</h2>
          <p>Monitor de pedidos</p>
        </div>
        <div className="card">
          <h2>📊 Admin</h2>
          <p>Gerenciamento completo</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
