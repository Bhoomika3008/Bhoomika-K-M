class Calculator:
    def __init__(self, a: "double", b: "double", operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def compute(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            return self.a / self.b if self.b != 0 else "Error: Division by zero"
        else:
            return "Invalid operation"

calc = Calculator(10.5, 2.5, "add")
print(calc.compute()) 