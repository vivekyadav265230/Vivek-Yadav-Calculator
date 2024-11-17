def calculate(num1, num2, operator):
  """Performs the specified arithmetic operation on two numbers."""
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      return "Error: Division by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operator"

while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    continue
  
  result = calculate(num1, num2, operator)
  print(f"Result: {result}")
  
  choice = input("Do you want to perform another calculation? (y/n): ")
  if choice.lower() != "y":
    break

print("Calculator closed.")
