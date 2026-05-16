# 🚀 Guia de Instalação

## Pré-requisitos

- Node.js 16+
- PostgreSQL 12+
- npm ou yarn
- Git

## Passo 1: Clonar o Repositório

```bash
git clone https://github.com/marcrobert100/tronix.git
cd tronix
```

## Passo 2: Configurar Banco de Dados

### Criar banco de dados
```bash
psql -U postgres
```

No psql:
```sql
CREATE DATABASE pizzaria_db;
\c pizzaria_db
\i database/schema.sql
```

Ou execute diretamente:
```bash
psql -U postgres -f database/schema.sql
```

## Passo 3: Configurar Backend

```bash
cd backend
cp .env.example .env
```

Edite `.env` com suas configurações:
```
PORT=5000
DB_HOST=localhost
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_NAME=pizzaria_db
```

Instale dependências:
```bash
npm install
```

Inicie o servidor:
```bash
npm run dev
```

## Passo 4: Configurar Frontend

```bash
cd ../frontend
npm install
npm start
```

O app abrirá em `http://localhost:3000`

## Passo 5: Testar

### Health Check do Backend
```bash
curl http://localhost:5000/health
```

Resposta esperada:
```json
{
  "status": "OK",
  "timestamp": "2026-05-15T10:30:00.000Z"
}
```

## Troubleshooting

### PostgreSQL não está rodando
```bash
# macOS
brew services start postgresql

# Windows
net start PostgreSQL

# Linux
sudo systemctl start postgresql
```

### Porta 5000 já está em uso
```bash
# Mude em backend/.env
PORT=5001
```

### Dependências não instalando
```bash
rm -rf node_modules
npm cache clean --force
npm install
```
