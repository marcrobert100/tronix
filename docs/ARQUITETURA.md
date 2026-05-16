# 🏗️ Arquitetura do Sistema TRONIX

## Visão Geral

O sistema segue uma arquitetura de 3 camadas:

```
┌─────────────────────────────────────────┐
│         FRONTEND (React)                 │
│  - Garçom  - Caixa  - Cozinha  - Admin  │
└────────────────┬────────────────────────┘
                 │ HTTP/REST
┌────────────────┴────────────────────────┐
│    BACKEND (Node.js + Express)          │
│  - Autenticação                          │
│  - Lógica de negócio                     │
│  - Integração com MercadoPago            │
└────────────────┬────────────────────────┘
                 │ SQL
┌────────────────┴────────────────────────┐
│    BANCO DE DADOS (PostgreSQL)          │
│  - Usuários, Clientes, Produtos          │
│  - Pedidos, Pagamentos, Licença          │
└─────────────────────────────────────────┘
```

## Componentes Principais

### Backend
- Express.js para API REST
- PostgreSQL para persistência
- JWT para autenticação
- Multer para upload de imagens
- MercadoPago API para pagamentos

### Frontend
- React 18
- React Router para navegação
- Axios para requisições HTTP
- CSS puro (sem dependências extras)

## Fluxos Principais

### 1. Fluxo de Pedido
```
Garçom → Lança Pedido → Backend → Cozinha vê no Monitor
          ↓
      Pedido Pronto
          ↓
      Caixa Cobra (PIX/Cartão)
          ↓
      Robô Interage com Cliente
          ↓
      Pagamento Aprovado
```

### 2. Fluxo de Admin
```
Admin → Cadastra Produto com Imagem → Backend
    ↓
Armazena em PostgreSQL
    ↓
Atualiza Cardápio Digital Automaticamente
    ↓
Garçom e Clientes veem novo Produto
```

### 3. Fluxo de Licença
```
Sistema Inicia
    ↓
Verifica Data de Vencimento no Servidor
    ↓
Se válida → Libera Acesso
Se expirado → Bloqueia Tudo
Se 7 dias para expirar → Alerta
```
