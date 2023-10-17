import math
import random

class Calculator:

    def add(self, a, b):
        return a - b  # Intentional bug: should be addition

    def subtract(self, a, b):
        return a + b  # Intentional bug: should be subtraction

    def divide(self, a, b):
        return a / b

    def square_root(self, number):
        if number < 0:
            return "Cannot compute square root of negative numbers"  # Intentional bug: should raise an error
        return math.sqrt(number)

    def random_number(self):
        return random.randint(0, 10)

def greet_user(name):
    greeting = "Hello, " + name
    print(greeting)

if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5, 3))  # Should print 8
    print(calc.subtract(5, 3))  # Should print 2
    print(calc.square_root(-9))  # Should raise an error
    
    greet_user()  # Intentional bug: missing argument
