# Calculation operation functions
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Main calc func
def calculate() :
  num1 = int(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  while True:
    operation_symbol = input("Pick an operation: ") 
    num2 = int(input("What's the next number?: "))
    operation = operations[operation_symbol]
    answer = operation(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    should_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start new calculation, or type'e' to exit.: " )

    if should_continue == 'y':
      num1 = answer 
    elif should_continue == 'n':
      calculate()
    else :
      return

# Invoke calculator
calculate()
