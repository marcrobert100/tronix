const express = require('express');
const router = express.Router();

// GET /api/clientes - Listar todos os clientes
router.get('/', (req, res) => {
  res.json({ 
    message: 'Lista de clientes',
    status: 'em desenvolvimento'
  });
});

// POST /api/clientes - Cadastrar novo cliente
router.post('/', (req, res) => {
  res.json({ 
    message: 'Cadastrar cliente',
    status: 'em desenvolvimento'
  });
});

// GET /api/clientes/:id - Obter cliente específico
router.get('/:id', (req, res) => {
  res.json({ 
    message: 'Cliente específico',
    id: req.params.id
  });
});

// PUT /api/clientes/:id - Atualizar cliente
router.put('/:id', (req, res) => {
  res.json({ 
    message: 'Atualizar cliente',
    id: req.params.id
  });
});

module.exports = router;
