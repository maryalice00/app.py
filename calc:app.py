from flask import Flask
from operations import add, sub, mult, div

app=Flask(__name__)

@app.route("/add")
def do_add():

    a = int(request.arg.get("a"))
    a = int(request.arg.get("b"))
    result = add(a,b)
    return str(result)

@app.route("/sub")
def do_sub():
    a = int(request.arg.get("a"))
    a = int(request.arg.get("b"))
    result = subb(a,b)
    return str(result)

@app.route("/mult")
def do_mult():
    a = int(request.arg.get("a"))
    a = int(request.arg.get("b"))
    result = mult(a,b)
    return str(result)

@app.route("/div")
def do_div():
    a = int(request.arg.get("a"))
    a = int(request.arg.get("b"))
    result = div(a,b)
    return str(result)


operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
   
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)