from fastapi import FastAPI
app = FastAPI()

#minimal app - get request
@app.get('/', tags=['ROOT'])
async def root() -> dict:
    return{"Ping":"Pong"}



#Get --> Read Todo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return{"data": todos}


#Post --> Create Todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo:dict) -> dict:
    todos(todo)
    return {
        "data":"A todo has been added!"
    }

#Put --> Update Todo
@app.put("/todo/{id},", tags=["todos"])
async def update_todo(id:int, body:dict) -> dict:
    """
    loop over the todos list
    for each todos item in the todos list,
    if that id is equal to id you have entered,
    then the activity must be equal to the 
    activity in the body where you are going to update
    your activities.
    """
    for todo in todos:
        if int(todo['id']) == id:
            todo['Activity'] = body['Activity']
            return {
                "data": f"Todo with id {id} has been updated"
            }
        return {
            "data": f"Todo with this id {id} was not found!"
        }

#Delete --> Delete Todo
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if (todo["id"]) == id:
            todos.remove(todo)
            return {
                "data":f"Todo with id {id} has been deleted"
            }
        return {
            "data":f"This todo with id {id} wasn't found!"
        }

todos = [
    { 
        "id": "1",
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    { 
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]