import sympy as sp
import tkinter as tk

def solve_fixed_equations(values):
    try:
        # Define the variables
        x, y, z = sp.symbols('x y z')

        # Extract values from the input
        x_val = values.get('x', None)
        y_val = values.get('y', None)
        z_val = values.get('z', None)

        # Define the equations with fixed structures but variable values, using PEMDAS
        eq1 = (2 * x) + 11  # Parentheses for clarity
        eq2 = ((2 * z) + y) - 5  # Parentheses for correct order of operations
        eq3 = sp.Abs((y + z) - x)  # Absolute value, ensuring PEMDAS

        # Substitute provided values into equations and evaluate
        eq1_value = eq1.subs({x: x_val}) if x_val is not None else 'Value for X not provided'
        eq2_value = eq2.subs({y: y_val, z: z_val}) if y_val is not None and z_val is not None else 'Values for Y and Z not provided'
        eq3_value = eq3.subs({x: x_val, y: y_val, z: z_val}) if x_val is not None and y_val is not None and z_val is not None else 'Values for X, Y, and Z not provided'

        # Helper function to format numerical results without trailing zeros
        def format_result(value):
            if isinstance(value, (int, float, sp.Float, sp.Integer, sp.Rational)):
                # Convert SymPy number to float and format using general format
                return '{:g}'.format(float(value))
            else:
                return str(value)

        # Apply formatting to each equation's value
        eq1_value = format_result(eq1_value) if isinstance(eq1_value, (int, float, sp.Basic)) else eq1_value
        eq2_value = format_result(eq2_value) if isinstance(eq2_value, (int, float, sp.Basic)) else eq2_value
        eq3_value = format_result(eq3_value) if isinstance(eq3_value, (int, float, sp.Basic)) else eq3_value

        return {
            'Equation 1': eq1_value,
            'Equation 2': eq2_value,
            'Equation 3': eq3_value
        }
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    def calculate():
        try:
            x_val = float(entry_x.get())
            y_val = float(entry_y.get())
            z_val = float(entry_z.get())
        except ValueError:
            result_label.config(text="Please enter valid numeric values for X, Y, and Z.")
            return

        values = {'x': x_val, 'y': y_val, 'z': z_val}
        solutions = solve_fixed_equations(values)

        result_str = "\n".join([f"{eq}: {solution}" for eq, solution in solutions.items()])
        result_label.config(text=result_str)

    # Create the GUI window
    root = tk.Tk()
    root.title("Zombies Easter Egg Algebra Solver")

    # Create and place labels and entry fields for X, Y, Z
    tk.Label(root, text="Enter the value for X:").grid(row=0, column=0, padx=10, pady=5)
    entry_x = tk.Entry(root)
    entry_x.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Enter the value for Y:").grid(row=1, column=0, padx=10, pady=5)
    entry_y = tk.Entry(root)
    entry_y.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Enter the value for Z:").grid(row=2, column=0, padx=10, pady=5)
    entry_z = tk.Entry(root)
    entry_z.grid(row=2, column=1, padx=10, pady=5)

    # Create and place the Calculate button
    calculate_button = tk.Button(root, text="Calculate", command=calculate)
    calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Create and place the result label
    result_label = tk.Label(root, text="", justify="left")
    result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Run the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
