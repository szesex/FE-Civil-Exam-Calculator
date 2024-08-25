from flask import Flask, render_template, request
import sympy as sp
import math

app = Flask(__name__)

# Define any specific constants and functions for the FE Civil exam here
def manning_equation(n, A, R, S):
    """Calculates velocity using the Manning equation."""
    return (1/n) * (R**(2/3)) * (S**0.5)

def bernoulli_equation(P1, v1, z1, P2, v2, z2, rho, g=9.81):
    """Calculates energy using the Bernoulli equation."""
    term1 = P1/(rho*g) + (v1**2)/(2*g) + z1
    term2 = P2/(rho*g) + (v2**2)/(2*g) + z2
    return term1 - term2

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Extract the expression or values to compute from the form
        expression = request.form.get('expression')
        try:
            # Use eval to safely calculate the expression
            result = eval(expression, {"__builtins__": None}, {"math": math, "sp": sp, "manning": manning_equation, "bernoulli": bernoulli_equation})
        except Exception as e:
            result = f"Error: {e}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
