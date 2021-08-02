# implementaciones para trabajar con fastapi

from fastapi import  FastAPI
from pydantic import BaseModel
from typing import Optional

from .APY.inicio import router

from APY.database import Database as connection
from APY.database import User

#declaracion de objeto de la clase FaztApi
appApy = FastAPI(title="FastApi example",
                description="una pequeña prueba con el framework de FaztApi",
                version="1.0.0")


appApy.include_router(router.route)

class Items(BaseModel ):
    name : str
    price : float

#routes
#evento que se dispara al iniciar la API
@appApy.on_event('startup')
async def startup_event():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User])
    

@appApy.on_event('shutdown')
async def shutdown_event():
    if not connection.is_closed():
        connection.close()    

@appApy.get("/")
@appApy.get("/api")
async def index(): 
    return {"welcome ":"FastApi"}


@appApy.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@appApy.put("/item/{item_id}")
async def update_item(item_id : int , item : Items):
    return {"item_name": item.name  , "items_id" : item_id }

@appApy.get('/products')
async def getProductos():

    pass
    return {"productos":"una nueva de productos"}
