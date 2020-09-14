#!./venv_task/bin/python3
from bottle import run, route, view


class ToDoItem:
    def __init__(self, description):
        self.desc = description
        self.in_active = False

@route("/")
@view("index")
def index():
    tasks = [
                ToDoItem("начать работать"),
                ToDoItem("выучить django"),
                ToDoItem("написать сервер на bottle"),
                ToDoItem("начать работать"),
            ]
    return {"tasks": tasks}
    


run(host="localhost", port="8080")
