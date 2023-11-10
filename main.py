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
    # Enhanced HTML content with more functionality and styling
    return """
    <html>
        <head>
            <title>FastAPI Greetings</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { margin-bottom: 20px; }
                .endpoint { background-color: #f4f4f4; padding: 10px; }
            </style>
        </head>
        <body>
            <h1>Welcome to the FastAPI Greetings API!</h1>

            <div class="container">
                <div class="endpoint">
                    <h2>Create a Greeting</h2>
                    <form action="/greetings/" method="post">
                        <input type="number" name="id" placeholder="ID" required>
                        <input type="text" name="message" placeholder="Greeting Message" required>
                        <button type="submit">Create</button>
                    </form>
                </div>

                <div class="endpoint">
                    <h2>Read All Greetings</h2>
                    <p><a href="/greetings/all">View all greetings</a></p>
                </div>

                <div class="endpoint">
                    <h2>Update a Greeting</h2>
                    <form action="/greetings/{greeting_id}" method="put">
                        <input type="number" name="greeting_id" placeholder="Greeting ID" required>
                        <input type="text" name="message" placeholder="New Greeting Message" required>
                        <button type="submit">Update</button>
                    </form>
                </div>

                <div class="endpoint">
                    <h2>Delete a Greeting</h2>
                    <form action="/greetings/{greeting_id}" method="delete">
                        <input type="number" name="greeting_id" placeholder="Greeting ID" required>
                        <button type="submit">Delete</button>
                    </form>
                </div>
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
