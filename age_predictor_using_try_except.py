# Age predictor using try/except

try:
  age = int(input('Enter your age:'))
  print(f'Next year: {age + 1}')

except ValueError:
  print('Invalid input!')

