# A dictionary to store greetings with an ID as the key and the greeting message as the value
greetings = {
    1: "Hello, World!",
    2: "Howdy, Partner!",
    3: "Greetings, Earthling!",
    4: "Salutations and Respect!",
    5: "Hey there, Universe!"
}

def get_all_greetings():
    return greetings

def create_greeting(id: int, message: str):
    if id in greetings:
        return {"error": "Greeting with this ID already exists."}
    greetings[id] = message
    return {"id": id, "message": message}

def get_greeting(greeting_id: int):
    if greeting_id not in greetings:
        return {"error": "Greeting not found."}
    return {"message": greetings[greeting_id]}

def update_greeting(greeting_id: int, message: str):
    if greeting_id not in greetings:
        return {"error": "Greeting not found."}
    greetings[greeting_id] = message
    return {"message": "Greeting updated successfully."}

def delete_greeting(greeting_id: int):
    if greeting_id not in greetings:
        return {"error": "Greeting not found."}
    del greetings[greeting_id]
    return {"message": "Greeting deleted successfully."}
