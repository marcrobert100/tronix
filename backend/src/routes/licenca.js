const express = require('express');
const router = express.Router();

// GET /api/licenca/info - Informações da licença
router.get('/info', (req, res) => {
  res.json({ 
    message: 'Informações da licença',
    status: 'em desenvolvimento'
  });
});

// POST /api/licenca/renovar - Renovar licença
router.post('/renovar', (req, res) => {
  res.json({ 
    message: 'Renovar licença',
    status: 'em desenvolvimento'
  });
});

// GET /api/licenca/status - Verificar status da licença
router.get('/status', (req, res) => {
  res.json({ 
    message: 'Status da licença',
    status: 'em desenvolvimento'
  });
});

module.exports = router;
