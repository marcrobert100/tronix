const express = require('express');
const router = express.Router();

// POST /api/pagamentos - Processar pagamento
router.post('/', (req, res) => {
  res.json({ 
    message: 'Processar pagamento via MercadoPago',
    status: 'em desenvolvimento'
  });
});

// GET /api/pagamentos/status/:id - Verificar status do pagamento
router.get('/status/:id', (req, res) => {
  res.json({ 
    message: 'Status do pagamento',
    id: req.params.id
  });
});

// POST /api/pagamentos/webhook - Webhook MercadoPago
router.post('/webhook', (req, res) => {
  res.json({ 
    message: 'Webhook MercadoPago',
    status: 'em desenvolvimento'
  });
});

module.exports = router;
