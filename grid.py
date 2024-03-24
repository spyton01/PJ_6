import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Error: Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets for numbers
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

# Operator dropdown menu
operator = tk.StringVar(root)
operator.set('+')  # default value
operator_dropdown = tk.OptionMenu(root, operator, '+', '-', '*', '/')
operator_dropdown.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

# Button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# Label to display result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()