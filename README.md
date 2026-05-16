# 🍕 Sistema de Gestão de Pizzaria - TRONIX

Sistema completo de gestão para pizzaria com integração de pagamento via robô, controle de pedidos, admin completo e relatórios.

## 📋 Funcionalidades

### 🤖 Robô do Caixa
- Pagamento via PIX e Cartão
- Áudio e vídeo interativo
- Vocabulário diversificado
- Feedback visual e sonoro

### 🧑‍💼 Garçom
- Lançamento de pedidos via tablet/notebook
- Interface intuitiva
- Acesso via rede local

### 👨‍🍳 Cozinha
- Monitor em tempo real
- Impressão de pedidos
- Status de preparação

### 📊 Admin
- Cadastro de produtos com upload de imagens
- Gerenciamento de clientes
- Controle de licença com data de validade
- Relatórios de vendas
- Cardápio digital

## 🛠️ Tecnologias

- **Backend**: Node.js + Express
- **Frontend**: React
- **Banco de Dados**: PostgreSQL
- **Pagamento**: MercadoPago (PIX + Cartão)
- **Autenticação**: JWT
- **Upload de Imagens**: Multer

## 📁 Estrutura do Projeto

```
tronix/
├── backend/                 # API Node.js
├── frontend/               # React App
├── database/               # Scripts SQL
├── docs/                   # Documentação
└── README.md
```

## 🚀 Como Começar

### Pré-requisitos
- Node.js 16+
- PostgreSQL 12+
- npm ou yarn

### Instalação Backend

```bash
cd backend
npm install
cp .env.example .env
npm run dev
```

### Instalação Frontend

```bash
cd frontend
npm install
npm start
```

## 📚 Documentação

Veja a pasta `docs/` para:
- [Arquitetura do Sistema](docs/ARQUITETURA.md)
- [API Documentation](docs/API.md)
- [Database Schema](docs/DATABASE.md)
- [Guia de Instalação](docs/INSTALACAO.md)

## 👥 Equipe

Desenvolvedor: marcrobert100

## 📝 Licença

MIT

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório.
