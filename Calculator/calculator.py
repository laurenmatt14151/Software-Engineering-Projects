
"""
1. Read line and identify numbers and arithmetic symbols
2. Perform order of operations
3. Return answer
"""
# Function to perform arithmetic operations
def apply_operation(operand1, operator, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            print("Error: Division by zero")
        else:
            return operand1 / operand2

def calculate(expression):
    # Remove whitespaces from the expression
    expression = expression.replace(" ", "")

    # Initialize variables
    current_number = ''
    numbers = []
    operators = []

    # Iterate through each character in the expression
    for char in expression:
        # If character is a digit or decimal add it to the current number to complete it
        if char.isdigit() or char == '.':
            current_number += char
        # Character is an operator, so add the completed current number to the list of numbers
        else:
            if current_number:
                numbers.append(float(current_number))
                current_number = ''
            # Add the operator to the list of operators
            operators.append(char)

    # Loop finishes with digit number in current_number, so adds it to the list of numbers
    if current_number:
        numbers.append(float(current_number))

    # Perform operations based on the order of operation
    for op in ['/', '*']:
        i = 0
        while i < len(operators):
            if operators[i] == op:
                result = apply_operation(numbers[i], operators[i], numbers[i+1])
                # Update the numbers and operators list with the result
                numbers = numbers[:i] + [result] + numbers[i + 2:]
                operators.pop(i)
            else:
                i += 1

    for op in ['+', '-']:
        i = 0
        while i < len(operators):
            if operators[i] == op:
                result = apply_operation(numbers[i], operators[i], numbers[i+1])
                # Update the numbers and operators list with the result
                numbers = numbers[:i] + [result] + numbers[i + 2:]
                operators.pop(i)
            else:
                i += 1

    # The final result is the only remaining number
        return round(numbers[0], 2)

def main():
    print("\n")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|     Welcome to my Calculator!      |")
    print("| Enter an expression. Example: 35/6 |")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")

    expression = input("Enter an arithmetic expression: ")
    result = calculate(expression)
    print("\n")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("         Result:", result)
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

if __name__ == "__main__": # Ensures main() is only executed if script is run 
    main();                # directly and not if imported as a module
