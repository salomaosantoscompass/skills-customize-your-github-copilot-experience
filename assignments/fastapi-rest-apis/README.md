# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST simples com FastAPI, aprendendo a criar endpoints, validar dados com Pydantic e retornar respostas HTTP adequadas.

## 📝 Tarefas

### 🛠️ Criar os Endpoints Básicos

#### Descrição
Implemente uma API para gerenciar uma lista de tarefas (to-do), começando com endpoints de leitura e criação.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI com endpoint `GET /` para health check.
- Implementar `GET /tasks` para listar todas as tarefas em memória.
- Implementar `POST /tasks` para criar uma nova tarefa.
- Retornar status code `201` ao criar com sucesso.

### 🛠️ Validar Dados de Entrada

#### Descrição
Use modelos Pydantic para garantir que os dados recebidos pela API tenham o formato esperado.

#### Requisitos
O programa concluído deve:

- Definir um modelo `TaskCreate` com os campos `title` e `done`.
- Tornar `title` obrigatório e não vazio.
- Rejeitar payloads inválidos com mensagens de erro automáticas do FastAPI.
- Gerar resposta JSON consistente para os endpoints principais.

### 🛠️ Implementar Busca por ID e Tratamento de Erros

#### Descrição
Adicione um endpoint para buscar uma tarefa específica e trate corretamente casos de recurso não encontrado.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para buscar tarefa por ID.
- Retornar `404` quando a tarefa não existir.
- Retornar JSON com os dados da tarefa quando existir.
- Manter o código organizado para facilitar adição de novos endpoints.
