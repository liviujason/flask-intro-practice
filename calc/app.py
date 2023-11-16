from operation import add, sub, multi, div
from flask import Flask, request
app = Flask(__name__)


@app.route('/add')
def func1():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)


@app.route('/sub')
def func2():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)


@app.route('/multi')
def func3():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = multi(a, b)
    return str(result)


@app.route('/div')
def func4():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)


@app.route('/math/<operation>')
def calculate(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    dict = {
        'add': add,
        'sub': sub,
        'multi': multi,
        'div': div
    }
    answer = dict[operation](a, b)
    return str(answer)
