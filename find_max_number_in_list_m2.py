# Find maximum number in list method-2

def find_max(numbers):
  largest = numbers[0]
  for i in range (len(numbers)):
    if numbers[i] > largest:
      largest = numbers[i]
  return largest

print(find_max([50, 20, 90]))
