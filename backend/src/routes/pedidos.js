const express = require('express');
const router = express.Router();

// GET /api/pedidos - Listar pedidos
router.get('/', (req, res) => {
  res.json({ 
    message: 'Lista de pedidos',
    status: 'em desenvolvimento'
  });
});

// POST /api/pedidos - Criar novo pedido
router.post('/', (req, res) => {
  res.json({ 
    message: 'Criar pedido',
    status: 'em desenvolvimento'
  });
});

// GET /api/pedidos/:id - Obter pedido específico
router.get('/:id', (req, res) => {
  res.json({ 
    message: 'Pedido específico',
    id: req.params.id
  });
});

// PUT /api/pedidos/:id/status - Atualizar status do pedido
router.put('/:id/status', (req, res) => {
  res.json({ 
    message: 'Atualizar status do pedido',
    id: req.params.id
  });
});

module.exports = router;
