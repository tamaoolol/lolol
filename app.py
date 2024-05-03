from flask import Flask, jsonify, request

app = Flask(__name__)

def process_operation(op, a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return {"status": False, "answer": "ARGS_PARSING_ERROR"}
    
    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        if b == 0:
            return {"status": False, "answer": "DIVISION_BY_ZERO"}
        result = a / b
    else:
        return {"status": False, "answer": "INVALID_OPERATION"}

    return {"status": True, "answer": f"{result:.4f}"}

@app.route('/<operation>/<num1>/<num2>')
def arithmetic(operation, num1, num2):
    return jsonify(process_operation(operation, num1, num2))

if __name__ == '__main__':
    app.run(debug=True)