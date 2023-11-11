from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # Importing HTMLResponse to enable returning HTML content
from pydantic import BaseModel  # BaseModel from Pydantic is used to define data models
from typing import Dict  # Importing Dict for type hinting
import os

port = int(os.environ.get("PORT", 8000))


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
    # Returns refined HTML content with descriptions and a link to the GitHub repository
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
            h1, p, ul {
                text-align: left;
                margin-left: auto;
                margin-right: auto;
                max-width: 600px;
            }
            .btn {
                display: block;
                width: 60%;
                padding: 10px 20px;
                margin: 20px auto;
                background: #333;
                color: #fff;
                border: none;
                cursor: pointer;
                text-decoration: none;
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
            code {
                background-color: #eee;
                padding: 2px 6px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the FastAPI Greetings API!</h1>
            <p>This is a simple API built with FastAPI following the MVC pattern to handle CRUD operations on greetings.</p>
            
            <ul>
                <li>To <strong>create</strong> a greeting, send a POST request to <code>/greetings/</code> with an ID and message.</li>
                <li>To <strong>read</strong> all greetings, click the button below or send a GET request to <code>/greetings/</code>.</li>
                <li>To <strong>update</strong> a greeting, send a PUT request to <code>/greetings/{id}</code> with a new message.</li>
                <li>To <strong>delete</strong> a greeting, send a DELETE request to <code>/greetings/{id}</code>.</li>
            </ul>
            
            <p>You can test these API endpoints using <code>curl</code>, Postman, or any other HTTP client.</p>
            
            <a href='/greetings/' class="btn">View All Greetings</a>
            
            <p>Check out the GitHub repository for this project:</p>
            <p><a href="https://github.com/Brandon-Alvarez-03/Fast_API_Quickstart" target="_blank">FastAPI Quickstart on GitHub</a></p>
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
