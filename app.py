import math
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    try:
        a = float(a) if a is not None and a != "" else None
        b = float(b) if b is not None and b != "" else None
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid number input"}), 400

    result = None
    error = None

    try:
        # Basic operations
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                error = "Division by zero"
            else:
                result = a / b
        elif operation == "modulo":
            if b == 0:
                error = "Division by zero"
            else:
                result = a % b
        elif operation == "power":
            result = a ** b

        # Advanced unary operations
        elif operation == "sqrt":
            if a < 0:
                error = "Cannot take square root of negative number"
            else:
                result = math.sqrt(a)
        elif operation == "cbrt":
            result = a ** (1 / 3) if a >= 0 else -((-a) ** (1 / 3))
        elif operation == "abs":
            result = abs(a)
        elif operation == "factorial":
            if a < 0 or a != int(a):
                error = "Factorial requires a non-negative integer"
            else:
                result = math.factorial(int(a))
        elif operation == "ln":
            if a <= 0:
                error = "Logarithm requires a positive number"
            else:
                result = math.log(a)
        elif operation == "log10":
            if a <= 0:
                error = "Logarithm requires a positive number"
            else:
                result = math.log10(a)
        elif operation == "log2":
            if a <= 0:
                error = "Logarithm requires a positive number"
            else:
                result = math.log2(a)
        elif operation == "exp":
            result = math.exp(a)
        elif operation == "floor":
            result = math.floor(a)
        elif operation == "ceil":
            result = math.ceil(a)
        elif operation == "round":
            result = round(a)
        elif operation == "reciprocal":
            if a == 0:
                error = "Cannot take reciprocal of zero"
            else:
                result = 1 / a
        elif operation == "square":
            result = a ** 2
        elif operation == "cube":
            result = a ** 3
        elif operation == "negate":
            result = -a
        elif operation == "percent":
            result = a / 100

        # Trigonometric (input in degrees)
        elif operation == "sin":
            result = math.sin(math.radians(a))
        elif operation == "cos":
            result = math.cos(math.radians(a))
        elif operation == "tan":
            result = math.tan(math.radians(a))
        elif operation == "asin":
            if a < -1 or a > 1:
                error = "asin requires input between -1 and 1"
            else:
                result = math.degrees(math.asin(a))
        elif operation == "acos":
            if a < -1 or a > 1:
                error = "acos requires input between -1 and 1"
            else:
                result = math.degrees(math.acos(a))
        elif operation == "atan":
            result = math.degrees(math.atan(a))

        # Hyperbolic
        elif operation == "sinh":
            result = math.sinh(a)
        elif operation == "cosh":
            result = math.cosh(a)
        elif operation == "tanh":
            result = math.tanh(a)

        # Constants
        elif operation == "pi":
            result = math.pi
        elif operation == "e":
            result = math.e
        elif operation == "tau":
            result = math.tau

        else:
            error = f"Unknown operation: {operation}"

    except OverflowError:
        error = "Result too large"
    except Exception as e:
        error = str(e)

    if error:
        return jsonify({"error": error}), 400

    # Format result nicely
    if isinstance(result, float):
        if result == int(result) and abs(result) < 1e15:
            result = int(result)
        else:
            result = round(result, 10)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
