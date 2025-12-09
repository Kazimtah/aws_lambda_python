class Calculator:

    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def subtract(a,b):
        return a-b
    
    @staticmethod
    def mult(a, b):
        return a * b 
    
    @staticmethod
    def divide(a,b):
        if b != 0:
            return a/b
        raise ValueError("Can't divid by Zero")
kazim = Calculator.mult(3,5)
print(kazim)
print(Calculator.divide(45, 7))