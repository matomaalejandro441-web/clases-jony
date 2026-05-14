from pydantic import BaseModel
from datetime import date



class Clientebase(BaseModel):
    name: str
    age: int
    description: str | None = None


class Clientecrear(Clientebase):
    pass


class Cliente(Clientebase):
    id: int



class Facturabase(BaseModel):
    fecha: date
    cliente: Cliente
    valortotal: float


class Facturacrear(Facturabase):
    pass


class Factura(Facturabase):
    id: int


class Transaccionbase(BaseModel):
    descripcion: str
    factura: Factura


class Transaccioncrear(Transaccionbase):
    pass


class Transaccion(Transaccionbase):
    id: int