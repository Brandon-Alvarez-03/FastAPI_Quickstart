from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

class Greeting(BaseModel):
    message: str

app = FastAPI()

# We'll use this dictionary to store our greetings
greetings = {
    1: "Hello, World!",
    2: "Howdy, Partner!",
    3: "Greetings, Earthling!",
    4: "Salutations and Respect!",
    5: "Hey there, Universe!"
}


@app.get("/")
def read_root():
    return {"message": "Go to /greetings/all to see all greetings", 
            "link": "<a href='/greetings/all'>All Greetings</a>"}
  
@app.get("/greetings/all")
def get_all_greetings():
    return greetings

@app.post("/greetings/")
def create_greeting(id: int, greeting: Greeting):
    if id in greetings:
        return {"error": "Greeting with this ID already exists."}
    greetings[id] = greeting.message
    return greeting

@app.get("/greetings/{greeting_id}")
def read_greeting(greeting_id: int):
    if greeting_id not in greetings:
        return {"error": "Greeting not found."}
    return {"message": greetings[greeting_id]}

@app.put("/greetings/{greeting_id}")
def update_greeting(greeting_id: int, greeting: Greeting):
    if greeting_id not in greetings:
        return {"error": "Greeting not found."}
    greetings[greeting_id] = greeting.message
    return {"message": "Greeting updated successfully."}
  
@app.delete("/greetings/{greeting_id}")
def delete_greeting(greeting_id: int):
    if greeting_id not in greetings:
        return {"error": "Greeting not found."}
    del greetings[greeting_id]
    return {"message": "Greeting deleted successfully."}

