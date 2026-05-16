const express = require('express');
const router = express.Router();

// GET /api/admin/dashboard - Dashboard admin
router.get('/dashboard', (req, res) => {
  res.json({ 
    message: 'Dashboard admin',
    status: 'em desenvolvimento'
  });
});

// POST /api/admin/usuarios - Criar usuário admin
router.post('/usuarios', (req, res) => {
  res.json({ 
    message: 'Criar usuário admin',
    status: 'em desenvolvimento'
  });
});

// GET /api/admin/usuarios - Listar usuários
router.get('/usuarios', (req, res) => {
  res.json({ 
    message: 'Lista de usuários',
    status: 'em desenvolvimento'
  });
});

module.exports = router;
