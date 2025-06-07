def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First number as float
        num2: Second number as float
        operation: String specifying operation ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        Result of the operation as float, or error message as string for division by zero
    
    Raises:
        ValueError: If operation is not one of the supported types
    """
    operation = operation.lower().strip()  # Normalize input
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
