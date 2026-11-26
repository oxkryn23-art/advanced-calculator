# Advanced Calculator

A web calculator with basic, scientific and trigonometric modes, built with Python (Flask) and vanilla JavaScript.
The math runs on the server through a small JSON API.

## Features

- **Basic mode:** addition, subtraction, multiplication, division, percentages and sign toggle
- **Scientific mode:** powers (x², x³, xʸ), roots, reciprocal, absolute value, factorial, logarithms (ln, log₁₀,
  log₂), the exponential eˣ, rounding (floor, ceil, round), modulo and the constants π, e and τ
- **Trigonometric mode:** sin, cos, tan, their inverses (arcsin, arccos, arctan) and the hyperbolic functions (sinh,
  cosh, tanh), all in degrees
- **Calculation history:** view and reuse previous results
- **Keyboard support:** the whole calculator can be used from the keyboard
- **Error handling:** division by zero and invalid input return a clear message

## Quick start

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000 in your browser.

## Tech stack

- Python 3 + Flask (the `/calculate` JSON endpoint)
- HTML, CSS and vanilla JavaScript (the interface)

## Project structure

```
advanced-calculator/
├── app.py              # Flask server and the calculation API
├── requirements.txt
└── templates/
    └── index.html      # the calculator interface
```
