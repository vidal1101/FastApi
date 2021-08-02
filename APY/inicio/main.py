from fastapi import APIRouter 

router = APIRouter(prefix="/inicio")

router.get("/get-users")
async def fethinicio():
    return {"prueba":"api router "}

