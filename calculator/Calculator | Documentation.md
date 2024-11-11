# Python Calculator Documentation

This documentation provides details for a simple command-line calculator as well as a graphical calculator application using the `tkinter` library.

## Command-Line Calculator

This is a simple Python program for performing basic arithmetic operations: addition, subtraction, multiplication, and division.

### Functions

The program defines four functions to perform each arithmetic operation:

- **`add(num1, num2)`**: Returns the sum of `num1` and `num2`.
- **`subtract(num1, num2)`**: Returns the difference between `num1` and `num2`.
- **`multiply(num1, num2)`**: Returns the product of `num1` and `num2`.
- **`divide(num1, num2)`**: Returns the result of dividing `num1` by `num2`.

### Usage

1. Run the script in a Python environment.
2. Select the desired operation by entering a number (1 to 4) corresponding to:
   - **1**: Addition
   - **2**: Subtraction
   - **3**: Multiplication
   - **4**: Division
3. Input the two numbers for the calculation.
4. The program outputs the result of the selected operation.

### Example

```python
Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide
Select operations form 1, 2, 3, 4: 1
Enter first number: 5
Enter second number: 3
5 + 3 = 8
```

---

## GUI Calculator

This calculator provides a graphical interface using the `tkinter` library. It allows users to perform arithmetic operations through buttons.

### Setup

To install `tkinter`, use the following command:

```bash
pip install tkinter
```

Then, import the necessary `tkinter` modules in your script:

```python
import tkinter as tk
import tkinter.messagebox
```

### Usage

1. Run the script to open the calculator window.
2. Use the on-screen buttons to input numbers and operations:
   - **Numbers**: 0–9 buttons.
   - **Operations**: `+`, `-`, `*`, `/`.
   - **Equal (`=`)**: Evaluates the entered expression.
   - **Clear**: Clears the input field.

### Example

The GUI includes buttons for all digits, basic operations, an equal sign, and a clear button. The result of each calculation is displayed in the input field.

### Functions

- **`myclick(number)`**: Inserts the clicked number or operator into the entry field.
- **`equal()`**: Evaluates the expression in the entry field and displays the result. If the expression is invalid, it shows a syntax error.
- **`clear()`**: Clears the entry field.

This provides a fully functional calculator with a straightforward user interface for basic arithmetic operations.