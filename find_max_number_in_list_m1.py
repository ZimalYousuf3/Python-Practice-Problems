# Findinf maximum number method-1

def find_max(numbers):
  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
  return largest

print(find_max([50, 20, 90]))
