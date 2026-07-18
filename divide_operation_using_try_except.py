# Wrap a divide operation in try/except to catch division by zero

try:
  num_1 = float(input('Enter 1st number:'))
  num_2 = float(input('Enter 2nd number:'))
  result = num_1/num_2
  print(f'Result: {result}')

except ZeroDivisionError:
  print(f'Cannot divide by zero!')
