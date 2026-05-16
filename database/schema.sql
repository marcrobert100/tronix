-- Criar banco de dados
CREATE DATABASE IF NOT EXISTS pizzaria_db;
\c pizzaria_db;

-- Usuários (Admin, Garçom, etc)
CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  senha VARCHAR(255) NOT NULL,
  tipo VARCHAR(20) NOT NULL DEFAULT 'garcom', -- admin, garcom, cozinha, caixa
  ativo BOOLEAN DEFAULT true,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Clientes
CREATE TABLE clientes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  telefone VARCHAR(20),
  email VARCHAR(100),
  endereco TEXT,
  tipo VARCHAR(20) DEFAULT 'padrao', -- padrao, vip, bloqueado
  ativo BOOLEAN DEFAULT true,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Categorias de Produtos
CREATE TABLE categorias (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(50) NOT NULL UNIQUE,
  descricao TEXT,
  ativo BOOLEAN DEFAULT true,
  ordem INT DEFAULT 0,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Produtos (Pizzas, Bebidas, etc)
CREATE TABLE produtos (
  id SERIAL PRIMARY KEY,
  categoria_id INT REFERENCES categorias(id),
  nome VARCHAR(100) NOT NULL,
  descricao TEXT,
  preco_inteiro DECIMAL(10, 2) NOT NULL,
  preco_meio DECIMAL(10, 2),
  ingredientes TEXT,
  imagem_url VARCHAR(255),
  tipo VARCHAR(20) DEFAULT 'pizza', -- pizza, bebida, sobremesa, etc
  ativo BOOLEAN DEFAULT true,
  pausado BOOLEAN DEFAULT false,
  especial BOOLEAN DEFAULT false, -- novidade, recomendacao, promocao
  ordem INT DEFAULT 0,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Pedidos
CREATE TABLE pedidos (
  id SERIAL PRIMARY KEY,
  cliente_id INT REFERENCES clientes(id),
  usuario_id INT REFERENCES usuarios(id),
  total DECIMAL(10, 2) NOT NULL,
  status VARCHAR(20) DEFAULT 'pendente', -- pendente, preparando, pronto, entregue, cancelado
  tipo_entrega VARCHAR(20) DEFAULT 'consumo', -- consumo, entrega, retirada
  observacoes TEXT,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Itens do Pedido
CREATE TABLE pedido_itens (
  id SERIAL PRIMARY KEY,
  pedido_id INT REFERENCES pedidos(id),
  produto_id INT REFERENCES produtos(id),
  quantidade INT NOT NULL,
  preco_unitario DECIMAL(10, 2) NOT NULL,
  tamanho VARCHAR(20) DEFAULT 'inteiro', -- inteiro, meio
  observacoes TEXT,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Pagamentos
CREATE TABLE pagamentos (
  id SERIAL PRIMARY KEY,
  pedido_id INT REFERENCES pedidos(id),
  metodo VARCHAR(20) NOT NULL, -- pix, cartao, dinheiro
  valor DECIMAL(10, 2) NOT NULL,
  status VARCHAR(20) DEFAULT 'pendente', -- pendente, aprovado, recusado
  transacao_id VARCHAR(100),
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Licença
CREATE TABLE licenca (
  id SERIAL PRIMARY KEY,
  data_inicio DATE NOT NULL,
  data_vencimento DATE NOT NULL,
  ativa BOOLEAN DEFAULT true,
  chave_licenca VARCHAR(255) UNIQUE,
  notificado_7dias BOOLEAN DEFAULT false,
  notificado_1dia BOOLEAN DEFAULT false,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Logs de Auditoria
CREATE TABLE audit_logs (
  id SERIAL PRIMARY KEY,
  usuario_id INT REFERENCES usuarios(id),
  acao VARCHAR(100) NOT NULL,
  tabela VARCHAR(50) NOT NULL,
  registro_id INT,
  dados_anteriores JSONB,
  dados_novos JSONB,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_produtos_categoria ON produtos(categoria_id);
CREATE INDEX idx_pedidos_cliente ON pedidos(cliente_id);
CREATE INDEX idx_pedidos_status ON pedidos(status);
CREATE INDEX idx_pedidos_criado_em ON pedidos(criado_em);
CREATE INDEX idx_pagamentos_pedido ON pagamentos(pedido_id);
CREATE INDEX idx_licenca_vencimento ON licenca(data_vencimento);
