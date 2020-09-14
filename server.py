#!./venv_task/bin/python3
from bottle import run, route, view, static_file, redirect, request


class ToDoItem:
    def __init__(self, description, unique_id):
        self.desc = description
        self.in_active = False
        self.uid = unique_id

    def __str__(self):
        return self.desc.lower()
    
tasks_db = {
        1: ToDoItem("начать работать", 1),
        2: ToDoItem("выучить django", 2),
        3: ToDoItem("написать сервер на bottle", 3),
        4: ToDoItem("начать работать", 4),
                }
    


@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")

@route("/api/delete/<uid:int>")
def api_delete(uid):
    tasks_db.pop(uid)
    return redirect("/")

@route("api/complete/uid:int")
def api_complete(uid):
    tasks_db[uid].in_active = True
    return "Ok"

@route("/")
@view("index")
def index():
    tasks = tasks_db.values()
    return {"tasks": tasks}
    
@route('/add_task', method="POST")
def add_task():
    desc = request.POST.description.strip()
    if len(desc) > 0:
        new_uid = max(tasks_db.keys()) + 1
        t = ToDoItem(desc, new_uid)
        tasks_db[new_uid] = t
    return redirect("/")

run(host="localhost", port="8080")
