from fastapi import APIRouter

routerGet = APIRouter(prefix='/getusers')

@routerGet.get('/users')
async def getUsers():
    return {"Usuarios":"get users"}