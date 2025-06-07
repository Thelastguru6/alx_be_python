def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations on two numbers.
    
    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
    float or str: Result of the operation, or error message for division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':  # Note: There's a typo here (should be 'multiply')
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
