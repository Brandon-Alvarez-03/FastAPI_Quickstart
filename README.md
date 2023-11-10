# Quickstart Guide for FastAPI Project

This guide will walk you through setting up a basic FastAPI application on Windows, macOS, and Linux.

## Prerequisites

- Python 3.6+ installed on your system
- Basic familiarity with command line interfaces

## Setup Instructions

### 1. **Create a Project Directory**

Create a new directory for your FastAPI project and navigate into it.

```bash
mkdir my_fastapi_project
cd my_fastapi_project
```

### 2. **Create a Virtual Environment**

It's a good practice to create a virtual environment for your Python projects. This helps to manage dependencies and ensure that your project environment is isolated from the global Python installation.

**Windows:**

```bash
python -m venv venv
```

**macOS/Linux:**

```bash
python3 -m venv venv
```

### 3. **Activate the Virtual Environment**

**Windows:**

```bash
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

After activation, your command line prompt should change to indicate that the virtual environment is active.

### 4. **Install FastAPI and Uvicorn**

With your virtual environment active, install FastAPI and Uvicorn (an ASGI server).

```bash
pip install fastapi uvicorn
```

### 5. **Create Your FastAPI Application**

Create a file named `main.py` in your project directory and add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

### 6. **Create a .gitignore File**

To prevent certain files and directories (like `__pycache__` and `venv`) from being tracked by Git, create a `.gitignore` file in your project's root directory.

**Step 1:** Create a `.gitignore` file:

```bash
touch .gitignore
```

**Step 2:** Open the `.gitignore` file in a text editor and add the following lines:

```
__pycache__/
venv/
*.pyc
```

This tells Git to ignore the `__pycache__` directory, the `venv` directory, and all files ending with `.pyc`.

### 7. **Run the Application**

Start your FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reload so the server will restart after changes are made to the code.

### 8. **Access Your Application**

Your FastAPI application will be running at `http://127.0.0.1:8000`. Open this URL in a web browser to see your application running.

### 9. **Interactive API Documentation**

FastAPI automatically generates interactive API documentation. Access it at `http://127.0.0.1:8000/docs`.

### API Endpoints

This application provides a simple CRUD API for greetings.

- `POST /greetings/`: Create a new greeting. Requires an `id` and a `message`.
- `GET /greetings/{greeting_id}`: Retrieve a greeting by its `id`.
- `PUT /greetings/{greeting_id}`: Update a greeting by its `id`.
- `DELETE /greetings/{greeting_id}`: Delete a greeting by its `id`.

### API Endpoints and Testing with `curl`

This application provides a simple CRUD API for greetings. Below are the `curl` commands to test each endpoint.

### Create a Greeting (POST)

To create a new greeting:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/greetings/?id=1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"message": "Hello, World!"}'
```

### Read a Greeting (GET)

To retrieve a greeting by its ID:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/greetings/1' \
  -H 'accept: application/json'
```

### Update a Greeting (PUT)

To update an existing greeting:

```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/greetings/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"message": "Hello, Universe!"}'
```

### Delete a Greeting (DELETE)

To delete a greeting:

```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/greetings/1' \
  -H 'accept: application/json'
```

These `curl` commands allow you to interact with the API directly from the command line. Ensure your FastAPI application is running before executing these commands.

### Additional Notes

- Deactivate your virtual environment when you're done working on the project by typing `deactivate` in your terminal.
- For more advanced features and detailed documentation, visit [FastAPI's official documentation](https://fastapi.tiangolo.com/).
