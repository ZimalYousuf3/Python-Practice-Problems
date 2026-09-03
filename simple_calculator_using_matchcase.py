# Simple Calculator using match case

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
op = input("Enter the operation (+,-,*,/): ")

match op:
  
  case "+":
    print(f'{num_1} + {num_2} = {num_1+num_2}')

  case "-":
    print(f'{num_1} - {num_2} = {num_1-num_2}')

  case "*":
    print(f'{num_1} x {num_2} = {num_1*num_2}')

  case "/":
    if num_2 == 0:
      print("ERROR! Cannot divide by zero.")
    else:
      print(f'{num_1} / {num_2} = {num_1/num_2}')

  case _:
    print("Invalid Operator!")
