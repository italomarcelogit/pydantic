from datetime import datetime
from pydantic import BaseModel, PositiveInt
from pydantic import ValidationError

class Pedido(BaseModel):
    id: int  
    nick_cliente: str = 'Maria José' 
    mesa: int
    pedido_ts: datetime | None  
    opcao: dict[str, PositiveInt]  

def exibe(pedidoID):
  print(Pedido(**pedidoID))

pedidos = [
  { #dados OK
    'id': 122, 
    'nick_cliente': 'Italo',
    'mesa': 1,
    'pedido_ts': '2023-12-20 19:22',  
    'opcao': { 'id_taca_vinho': 9, 'id_broto_pizza': 7, 'id_sobremesa': 1}
  }, 
  { #dados não Ok, id_sobremesa não é inteiro 
    'id': 123,
    'nick_cliente': 'Ana',
    'mesa': 3,
    'pedido_ts': '2023-12-20 19:23',  
    'opcao': { 'id_taca_vinho': 5, 'id_broto_pizza': 2, 'id_sobremesa': 'l'}
  },
]


try:
    [exibe(p) for p in pedidos]
except ValidationError as e:
    print(e.errors())
