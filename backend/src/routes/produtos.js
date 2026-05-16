const express = require('express');
const router = express.Router();

// GET /api/produtos - Listar todos os produtos
router.get('/', (req, res) => {
  res.json({ 
    message: 'Lista de produtos',
    status: 'em desenvolvimento'
  });
});

// POST /api/produtos - Criar novo produto
router.post('/', (req, res) => {
  res.json({ 
    message: 'Criar produto endpoint',
    status: 'em desenvolvimento'
  });
});

// GET /api/produtos/:id - Obter produto específico
router.get('/:id', (req, res) => {
  res.json({ 
    message: 'Produto específico',
    id: req.params.id
  });
});

// PUT /api/produtos/:id - Atualizar produto
router.put('/:id', (req, res) => {
  res.json({ 
    message: 'Atualizar produto',
    id: req.params.id
  });
});

// DELETE /api/produtos/:id - Deletar produto
router.delete('/:id', (req, res) => {
  res.json({ 
    message: 'Deletar produto',
    id: req.params.id
  });
});

module.exports = router;
