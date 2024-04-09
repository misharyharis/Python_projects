from art import logo
print(logo)
#sum
def add(n1, n2):
  return n1 + n2
#subtract
def subtract(n1, n2):
  return n1-n2

#multi
def multiply(n1, n2):
  return n1*n2

#divide
def divide(n1, n2):
  return n1/n2

calc={
  "+" : add,
  "-" : subtract,
  "*" : multiply, 
  "/" : divide
}

def calculator():
  num1=float(input("What is the first number? "))
  
  for symbol in calc:
    print(symbol)
  
  is_continue=True
  while is_continue:
     
    operation_symbol=input("Pick an operation  ")
    num2=float(input("What is the next number? "))
    calc_function=calc[operation_symbol]
    answer=calc_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit ") == "y":
      num1=answer
    else:
      is_continue=False
      calculator()
calculator()