from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

list_clients = []

#models

class client(BaseModel):
    id: int
    name: str
    age: int
    description: str |None = None #NO OBLIGATORIO

@app.get('/')
def start():
    return {"message": "hello world"}

@app.get("/clientes")
def Listar_clientes():
    return {"clients": list_clients}

@app.post("/clientes" )
def create_clients(date_client: client):
    list_clients.append(date_client) #append agrega el cliente a la lista de clientes
    return {"message": "client created"}

#reto: crear un nuevo endponint y que me remote un solo cliente 
@app.get("/clientes/{id}")
def get_client(id: int):
    for client in list_clients:
        if client.id == id:
            return client
    return {"message": "client not found"}

@app.delete("/clientes/{id}")
def delete_client(id: int):
    for client in list_clients:
        if client.id == id:
            list_clients.remove(client) #remove elimina el cliente de la lista de clientes
            return {"message": "client deleted"}
    return {"message": "client not found"}

#uv pip list para ver las dependencias