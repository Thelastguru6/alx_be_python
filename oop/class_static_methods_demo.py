# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method that prints a class attribute and returns the product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

