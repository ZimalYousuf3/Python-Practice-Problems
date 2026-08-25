# Finding sum of even numbers in list

def sum_even(numbers):
  total = 0
  for num in numbers:
    if num % 2 == 0:
      total = total + num
  return total

print(sum_even([1,2,3,4,5,6,7,8,9]))
