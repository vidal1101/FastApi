from fastapi import APIRouter

router = APIRouter()

router.get("/inicio-router")
async def inicio():
    return {"prueba":"api router "}
