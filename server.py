#!./venv_task/bin/python3
from bottle import run, route, view, static_file, redirect, request
from db import ToDoItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
s = Session()


@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")


@route("/api/delete/<uid:int>")
def api_delete(uid):
    s.query(ToDoItem).filter(ToDoItem.uid == uid).delete()
    s.commit()
    return redirect("/")


@route("api/complete/uid:int")
def api_complete(uid):
    t = s.query(ToDoItem).filter(ToDoItem.uid == uid).first()
    t.in_active = True
    s.commit()
    return "Ok"


@route("/")
@view("index")
def index():
    tasks = s.query(ToDoItem).order_by(ToDoItem.uid)
    return {"tasks": tasks}
    
@route('/add_task', method="POST")
def add_task():
    desc = request.POST.description.strip()
    if len(desc) > 0:
        t = ToDoItem(desc)
        s.add(t)
        s.commit()
    return redirect("/")

run(host="localhost", port="8080")
