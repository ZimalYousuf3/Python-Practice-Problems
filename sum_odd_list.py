# Finind sum of odd numbers from list

def sum_odd(numbers):
  total = 0
  for num in numbers:
    if num % 2 != 0:
      total = total + num
  return total

print(sum_odd([1,2,3,4,5,6,7,8,9]))
