# 📚 Documentação da API

## Base URL
```
http://localhost:5000/api
```

## Autenticação
Todas as rotas (exceto login) requerem token JWT no header:
```
Authorization: Bearer {token}
```

## Rotas

### Auth
- `POST /auth/login` - Login de usuário
- `POST /auth/logout` - Logout

### Produtos
- `GET /produtos` - Listar produtos
- `GET /produtos/:id` - Obter produto
- `POST /produtos` - Criar produto
- `PUT /produtos/:id` - Atualizar produto
- `DELETE /produtos/:id` - Deletar produto

### Clientes
- `GET /clientes` - Listar clientes
- `GET /clientes/:id` - Obter cliente
- `POST /clientes` - Cadastrar cliente
- `PUT /clientes/:id` - Atualizar cliente

### Pedidos
- `GET /pedidos` - Listar pedidos
- `GET /pedidos/:id` - Obter pedido
- `POST /pedidos` - Criar pedido
- `PUT /pedidos/:id/status` - Atualizar status

### Pagamentos
- `POST /pagamentos` - Processar pagamento
- `GET /pagamentos/status/:id` - Status do pagamento

### Admin
- `GET /admin/dashboard` - Dashboard
- `POST /admin/usuarios` - Criar usuário
- `GET /admin/usuarios` - Listar usuários

### Relatórios
- `GET /relatorios/vendas` - Relatório de vendas
- `GET /relatorios/clientes` - Relatório de clientes
- `GET /relatorios/produtos` - Relatório de produtos

### Licença
- `GET /licenca/info` - Info da licença
- `GET /licenca/status` - Status da licença
- `POST /licenca/renovar` - Renovar licença
