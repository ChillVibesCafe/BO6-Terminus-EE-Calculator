# Terminus Easter Egg Algebra Solver

A simple GUI-based tool to solve algebraic puzzles in the 'Terminus' Zombies map from Black Ops 6. Users input X, Y, and Z values to quickly get results for three fixed equations, making it easier to solve in-game Easter eggs.

## Features

- Graphical User Interface (GUI) for ease of use.
- Takes inputs for variables X, Y, and Z.
- Solves three predefined equations based on the given values.
- Displays results without unnecessary trailing zeros.

## Equations

The algebra solver calculates the following three equations:

1. **Equation 1**: `2X + 11`
2. **Equation 2**: `(2Z + Y) - 5`
3. **Equation 3**: `|(Y + Z) - X|`

## Requirements

- Python 3.x
- `sympy` library: used for symbolic mathematics.
- `tkinter` library: used for creating the graphical interface (comes pre-installed with Python).

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:
   ```sh
   pip install sympy tkinter
   ```
   ```
   ```

## How to Use

Please note that you will need to find the values for X, Y, and Z within the game. This can be easily done by following a YouTube tutorial if needed.

1. Run the Python script:
   ```sh
   python algebra_solver.py
   ```
2. Enter the values for X, Y, and Z in the GUI.
3. Click **Calculate** to view the results of the three equations.

## Example

For X = 11, Y = 21, Z = 10, the output will be:

```
Equation 1: 33
Equation 2: 36
Equation 3: 20
```



