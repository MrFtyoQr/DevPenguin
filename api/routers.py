# api/routers.py
from fastapi import APIRouter, HTTPException#Importamos APIRouter y HTTPException de fastapi
from services.openrouter_service import OpenRouterService#Importamos la clase OpenRouterService de services.openrouter_service

router = APIRouter()#aqui creamos el router
service = OpenRouterService()#aqui inicializamos la clase OpenRouterService

@router.post("/ask")#aqui creamos la ruta /ask que recibe un metodo post
def ask_question(question: str):#aqui creamos el metodo ask_question que recibe un parametro question que es un string
    try:
        response = service.get_response(question)#aqui creamos la variable response que es el metodo get_response que se encuentra en la clase OpenRouterService que recibe un parametro question que es un string
        return {"response": response}#aqui retornamos un diccionario con la clave response y el valor response
    except Exception as e:#aqui manejamos la excepcion
        raise HTTPException(status_code=500, detail=str(e))#aqui lanzamos una excepcion HTTPException con el status_code 500 y el detalle de la excepcion