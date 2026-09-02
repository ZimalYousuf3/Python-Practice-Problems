# Simple Calculator

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
op = input("Enter the operation (+,-,*,/): ")

if op == "+":
  print(f'{num_1} + {num_2} = {num_1+num_2}')

elif op == "-":
  print(f'{num_1} - {num_2} = {num_1-num_2}')

elif op == "*":
  print(f'{num_1} x {num_2} = {num_1*num_2}')

elif op == "/":
  if num_2 == 0:
    print("ERROR! Cannot divide by zero.")
  else:
    print(f'{num_1} / {num_2} = {num_1/num_2}')

elif op == "**":
  print(f'{num_1} ^ {num_2} = {num_1**num_2}')

else:
  print("Invalid Operator!")
