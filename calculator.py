#calculator

def add (n1,n2):
    return n1 + n2

    
def substract (n1,n2):
    return n1 - n2
 

def divide (n1,n2):
    return n1 / n2
    

def multiply(n1,n2):
    return n1 * n2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}
def calculator():
    n1 =float(input("Enter  first number: "))
    #n2 = float(input("Enter n2: "))


    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1,n2)
            
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start again: ") == 'y':
            n1 = answer
            should_continue = True
        else:
            should_continue = False
            calculator()

calculator() 
