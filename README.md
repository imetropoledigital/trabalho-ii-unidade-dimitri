[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ori1I0wD)
# Trabalho II Unidade - FastAPI com MongoDB

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 
- MongoDB

## Estrutura do Projeto

```plaintext
trabalho-ii-unidade-dimitri/
├── app.py          
├── requirements.txt  
├── README.md       
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/imetropoledigital/trabalho-ii-unidade-dimitri.git
   cd trabalho-ii-unidade-dimitri
   ```

2. Instale as dependências:
   - Usando `pip`:
     ```bash
     pip install -r requirements.txt
     ```

3. Certifique-se de que o MongoDB está em execução na porta padrão `27017`. Caso necessário, configure a URL de conexão no código, no arquivo `app.py`.

## Execução

1. Inicie o servidor FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

2. Acesse a documentação interativa no navegador:
   - Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Rotas Disponíveis

### Operações CRUD Dinâmicas

#### Criar um documento
- **POST /{collection_name}**
- Exemplo:
  ```bash
  curl -X POST "http://127.0.0.1:8000/pessoa" \
       -H "Content-Type: application/json" \
       -d '{"data": {"name": "Maria", "age": 30}}'
  ```

#### Buscar documentos com filtros e projeção
- **GET /{collection_name}**
- Exemplo de busca com filtro:
  ```bash
  curl -X GET "http://127.0.0.1:8000/pessoa?query={\"name\":\"Maria\"}"
  ```
- Exemplo de projeção:
  ```bash
  curl -X GET "http://127.0.0.1:8000/pessoa?fields=name,age"
  ```

#### Buscar um documento por ID
- **GET /{collection_name}/{id}**
- Exemplo:
  ```bash
  curl -X GET "http://127.0.0.1:8000/pessoa/64a8b6d02b5432160db6ef50"
  ```

#### Atualizar um documento por ID
- **PUT /{collection_name}/{id}**
- Exemplo:
  ```bash
  curl -X PUT "http://127.0.0.1:8000/pessoa/64a8b6d02b5432160db6ef50" \
       -H "Content-Type: application/json" \
       -d '{"data": {"age": 31}}'
  ```

#### Excluir um documento por ID
- **DELETE /{collection_name}/{id}**
- Exemplo:
  ```bash
  curl -X DELETE "http://127.0.0.1:8000/pessoa/64a8b6d02b5432160db6ef50"
  ```

### Listar todas as coleções
- **GET /collections**
- Exemplo:
  ```bash
  curl -X GET "http://127.0.0.1:8000/collections"
  ```

