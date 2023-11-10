from fastapi import APIRouter, HTTPException
from .controllers import get_all_greetings, create_greeting, get_greeting, update_greeting, delete_greeting
from .models import Greeting

router = APIRouter()

@router.get("/greetings/")
def read_all_greetings():
    return get_all_greetings()

@router.post("/greetings/", response_model=Greeting)
def create_new_greeting(id: int, message: str):
    result = create_greeting(id, message)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/greetings/{greeting_id}", response_model=Greeting)
def read_greeting(greeting_id: int):
    result = get_greeting(greeting_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.put("/greetings/{greeting_id}", response_model=Greeting)
def update_existing_greeting(greeting_id: int, greeting: Greeting):
    result = update_greeting(greeting_id, greeting.message)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.delete("/greetings/{greeting_id}")
def delete_existing_greeting(greeting_id: int):
    result = delete_greeting(greeting_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
