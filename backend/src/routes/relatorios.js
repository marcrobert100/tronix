const express = require('express');
const router = express.Router();

// GET /api/relatorios/vendas - Relatório de vendas
router.get('/vendas', (req, res) => {
  res.json({ 
    message: 'Relatório de vendas',
    status: 'em desenvolvimento'
  });
});

// GET /api/relatorios/clientes - Relatório de clientes
router.get('/clientes', (req, res) => {
  res.json({ 
    message: 'Relatório de clientes',
    status: 'em desenvolvimento'
  });
});

// GET /api/relatorios/produtos - Relatório de produtos
router.get('/produtos', (req, res) => {
  res.json({ 
    message: 'Relatório de produtos',
    status: 'em desenvolvimento'
  });
});

module.exports = router;
