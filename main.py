from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # Importing HTMLResponse to enable returning HTML content
from pydantic import BaseModel  # BaseModel from Pydantic is used to define data models
from typing import Dict  # Importing Dict for type hinting

# Define a Pydantic model for the Greeting data structure
class Greeting(BaseModel):
    message: str  # Each Greeting has a 'message' field of type string

app = FastAPI()  # Create an instance of the FastAPI class

# A dictionary to store greetings with an ID as the key and the greeting message as the value
greetings = {
    1: "Hello, World!",
    2: "Howdy, Partner!",
    3: "Greetings, Earthling!",
    4: "Salutations and Respect!",
    5: "Hey there, Universe!"
}

# Define the root endpoint, which returns an HTML response
@app.get("/", response_class=HTMLResponse)
def read_root():
    # Returns refined HTML content with styling
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Greetings</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f7f7f7;
                color: #333;
                line-height: 1.6;
                margin: 0;
                padding: 30px;
                text-align: center;
            }
            .container {
                max-width: 700px;
                margin: auto;
                overflow: hidden;
                padding: 0 20px;
            }
            h1, p {
                text-align: center;
            }
            .btn {
                display: block;
                width: 100%;
                padding: 10px 20px;
                margin: 20px auto;
                background: #333;
                color: #fff;
                border: none;
                cursor: pointer;
            }
            .btn:hover {
                background: #555;
            }
            a {
                color: #333;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the FastAPI Greetings API!</h1>
            <p>Click the button below to view all greetings.</p>
            <a href='/greetings/' class="btn">View All Greetings</a>
        </div>
    </body>
    </html>
    """

# Endpoint to get all greetings
@app.get("/greetings/")
def get_all_greetings():
    return greetings  # Returns the entire dictionary of greetings

# Endpoint to create a new greeting
@app.post("/greetings/")
def create_greeting(id: int, greeting: Greeting):
    if id in greetings:
        # If the ID already exists in the dictionary, return an error message
        return {"error": "Greeting with this ID already exists."}
    greetings[id] = greeting.message  # Add the new greeting to the dictionary
    return greeting  # Return the newly created greeting

# Endpoint to read a specific greeting by ID
@app.get("/greetings/{greeting_id}")
def read_greeting(greeting_id: int):
    if greeting_id not in greetings:
        # If the ID is not found in the dictionary, return an error message
        return {"error": "Greeting not found."}
    return {"message": greetings[greeting_id]}  # Return the greeting message

# Endpoint to update an existing greeting
@app.put("/greetings/{greeting_id}")
def update_greeting(greeting_id: int, greeting: Greeting):
    if greeting_id not in greetings:
        # If the ID is not found in the dictionary, return an error message
        return {"error": "Greeting not found."}
    greetings[greeting_id] = greeting.message  # Update the greeting message
    return {"message": "Greeting updated successfully."}

# Endpoint to delete a greeting
@app.delete("/greetings/{greeting_id}")
def delete_greeting(greeting_id: int):
    if greeting_id not in greetings:
        # If the ID is not found in the dictionary, return an error message
        return {"error": "Greeting not found."}
    del greetings[greeting_id]  # Delete the greeting from the dictionary
    return {"message": "Greeting deleted successfully."}
