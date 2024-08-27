def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
      # Displaying available operations  
      for symbol in operations:
            print(symbol)
          
      operation_symbol = input("Pick an operation: ")
      num2 = float(input("What is the second number?: "))
      answer = operations[operation_symbol](num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")

      # Asks user to continue or start over
      choice = input(f"Type 'yes' to continue calculating with {answer} or type 'no' to start again")

      if choice == 'yes':
        num1 = answer # Updates num1 to the current answer
      else: 
        should_accumulate = False
        print("\n" * 20)
        calculator() # Restarts the calculator

calculator()
