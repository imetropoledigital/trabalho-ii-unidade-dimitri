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



