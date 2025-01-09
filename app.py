from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from bson import ObjectId
from typing import List, Optional
from pydantic import BaseModel
import json

# Configuração do MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["dynamic_database"]

# Inicialização da API
app = FastAPI()

# Modelo Base para Dados Genéricos
class GenericEntity(BaseModel):
    data: dict  # Validação de campos genéricos como um dicionário

# Criação dinâmica de coleções
@app.post("/{collection_name}")
async def create_entity(collection_name: str, entity: GenericEntity):
    """
    Cadastra um novo documento em uma coleção dinâmica.
    - `collection_name`: Nome da coleção onde o documento será inserido.
    """
    collection = db[collection_name]
    result = collection.insert_one(entity.data)
    return {"message": "Entity created successfully", "id": str(result.inserted_id)}

# Listagem de todas as entidades com projeção simples
@app.get("/{collection_name}")
async def get_all_entities(
    collection_name: str,
    query: str = Query(default="{}", alias="query"),
    fields: Optional[str] = Query(default=None, alias="fields"),
    skip: int = 0,
    limit: int = 10,
):
    """
    Retorna documentos de uma coleção com paginação e projeção.
    - `collection_name`: Nome da coleção a ser consultada.
    - `query`: Filtro em formato JSON.
    - `fields`: Campos a serem incluídos ou excluídos no formato `name`, `-name`, `name,age`.
    - `skip`: Número de documentos a ignorar.
    - `limit`: Número máximo de documentos a retornar.
    """
    try:
        # Convertendo o filtro de JSON para dicionário
        filter_query = json.loads(query)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid query format")

    # Construção da projeção
    projection = {}
    if fields:
        for field in fields.split(","):
            if field.startswith("-"):
                projection[field[1:]] = 0  # Excluir o campo
            else:
                projection[field] = 1  # Incluir o campo

    try:
        collection = db[collection_name]
        # Consulta no MongoDB
        entidades = list(
            collection.find(filter_query, projection).skip(skip).limit(limit)
        )
        # Convertendo ObjectId para string
        for entidade in entidades:
            entidade["_id"] = str(entidade["_id"])
        return entidades
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving entities: {str(e)}")

# Obter um único documento por ID
@app.get("/{collection_name}/{id}")
async def get_entity_by_id(collection_name: str, id: str):
    """
    Retorna um documento específico por ID.
    - `collection_name`: Nome da coleção.
    - `id`: ID do documento.
    """
    try:
        collection = db[collection_name]
        obj_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    entidade = collection.find_one({"_id": obj_id})
    if entidade:
        entidade["_id"] = str(entidade["_id"])  # Converte ObjectId para string
        return entidade
    raise HTTPException(status_code=404, detail="Entity not found")

# Atualizar documento por ID
@app.put("/{collection_name}/{id}")
async def update_entity(collection_name: str, id: str, entity: GenericEntity):
    """
    Atualiza um documento por ID.
    - `collection_name`: Nome da coleção.
    - `id`: ID do documento.
    - `entity`: Dados atualizados.
    """
    try:
        collection = db[collection_name]
        obj_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    result = collection.update_one({"_id": obj_id}, {"$set": entity.data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Entity not found")
    return {"message": "Entity updated successfully"}

# Excluir documento por ID
@app.delete("/{collection_name}/{id}")
async def delete_entity(collection_name: str, id: str):
    """
    Exclui um documento por ID.
    - `collection_name`: Nome da coleção.
    - `id`: ID do documento.
    """
    try:
        collection = db[collection_name]
        obj_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    result = collection.delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Entity not found")
    return {"message": "Entity deleted successfully"}
