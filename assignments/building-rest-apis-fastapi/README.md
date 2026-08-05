# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST com FastAPI para gerenciar produtos, praticando criação de endpoints, validação com Pydantic e tratamento de erros HTTP.

## 📝 Tarefas

### 🛠️	Criar Endpoints Básicos da API

#### Descrição
Implemente uma API com um endpoint de health check e endpoints para listar e criar produtos em memória.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI com endpoint `GET /` retornando status da API.
- Implementar `GET /products` para listar todos os produtos cadastrados.
- Implementar `POST /products` para criar um novo produto.
- Retornar status code `201` ao criar com sucesso.


### 🛠️	Validar Dados com Pydantic

#### Descrição
Use modelos Pydantic para validar os dados de entrada e garantir consistência nas respostas.

#### Requisitos
O programa concluído deve:

- Definir um modelo `ProductCreate` com campos `name`, `price` e `in_stock`.
- Exigir que `name` seja obrigatório e não vazio.
- Exigir que `price` seja maior que zero.
- Retornar erros de validação automáticos do FastAPI para payloads inválidos.


### 🛠️	Buscar por ID e Tratar Erros

#### Descrição
Adicione endpoint de busca por ID e trate corretamente casos em que o recurso não existe.

#### Requisitos
O programa concluído deve:

- Implementar `GET /products/{product_id}` para buscar produto por ID.
- Retornar `404` quando o produto não for encontrado.
- Retornar JSON com o produto quando ele existir.
- Manter o código organizado para facilitar extensão com novos endpoints.
