from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # Importing HTMLResponse to enable returning HTML content
from .routes import router as greetings_router

import os

port = int(os.environ.get("PORT", 8000))

app = FastAPI()

app.include_router(greetings_router)

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
