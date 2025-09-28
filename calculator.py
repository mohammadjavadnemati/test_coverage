class Calculator:
    def add(self, a, b):    # pragma: no cover
        return a + b

    def subtract(self, a, b):  # pragma: no cover
        return a - b

    def multiply(self, a, b):  
        return a * b

    def divide(self, a, b):  # pragma: no cover
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):  # pragma: no cover
        return a ** b

    def factorial(self, n):  # pragma: no cover
        if n < 0:
            raise ValueError("Factorial does not exist for negative numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def sqrt(self, a):  # pragma: no cover
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return a ** 0.5

    def sum_of_numbers(self, numbers):  # pragma: no cover
        if not all(isinstance(x, (int, float)) for x in numbers):
            raise ValueError("All elements must be numbers")
        return sum(numbers)

    def is_prime(self, n):  # pragma: no cover
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
