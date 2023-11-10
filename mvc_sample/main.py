from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # Importing HTMLResponse to enable returning HTML content
from .routes import router as greetings_router

app = FastAPI()

app.include_router(greetings_router)

# The root endpoint can remain here or be moved to the routes.py as well
@app.get("/", response_class=HTMLResponse)
def read_root():
    # Your HTML content goes here
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