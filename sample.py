Here is the fixed code:

```python
import math
import random

class Calculator:

    def add(self, a, b):
        return a + b  

    def subtract(self, a, b):
        return a - b  

    def divide(self, a, b):
        return a / b

    def square_root(self, number):
        if number < 0:
            return "Cannot compute square root of negative numbers"  
        return math.sqrt(number)

    def random_number(self):
        return random.randint(0, 10)

def greet_user(name):
    greeting = "Hello, " + name
    print(greeting)

if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5, 3))  
    print(calc.subtract(5, 3))  
    print(calc.square_root(-9))  
    
    greet_user("John")
```

Note: I fixed the error in the `greet_user()` function by providing a name argument when calling the function.