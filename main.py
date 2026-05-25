from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()    # app is the instance of FastAPI object

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/greet")
def greet():
    return {
        "message":"sam",
        "name" : "samules"
    }

@app.get("/greet/{name}")   #path parameter
def greet_name(name:str,age: Optional[int] = None):  # if query parameter is not given in url then by default it is None or any no. like 45 
    return {
        "message": f"the name is {name} and the age is {age}"
    }




class student(BaseModel):
    name: str
    age: int
    roll: int


@app.post("/creatstudent")
def create_student(student:student):
    return{
        "name": student.name,
        "age" : student.age,
        "roll": student.roll
    }
 