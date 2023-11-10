from pydantic import BaseModel

# Define a Pydantic model for the Greeting data structure
class Greeting(BaseModel):
    message: str  # Each Greeting has a 'message' field of type string
