def add(n1,n2): 
    return n1+n2
def subract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2    
def divide(n1,n2):
    return n1/n2
operations = {
    "+": add,
    "-": subract,
    "*": multiply,
    "/": divide,
    "**": lambda n1,n2: (n1**n2),
}
def calculate():
    should_continue = True
    num1 = float(input("Enter first number: "))
    while should_continue:
        for symbols in operations:
            print(symbols)
            operation_symbol = input("Pick an operation from the line above: ")
            num2 = float(input("Enter second number: "))
            ans = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {ans}")
            choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = ans
        else:
            should_continue = False
            print("\n"*100)
            calculate()
calculate()
