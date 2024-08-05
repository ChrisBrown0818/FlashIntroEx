from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)


@app.route("/sub")
def do_sub():
    """subtract a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result  = sub(a, b)

    return str(result)

@app.route("/mult")
def do_mult():
    """do multiply with a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route("/div")
def do_div():
    """ do div with a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)



Operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
}


@app.route("/math/<oper>")
def do_math(oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = Operators[oper](a, b)

    return str(result)




