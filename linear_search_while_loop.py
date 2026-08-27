# Linear Search through while loops

def linear_search(numbers, target):
  i = 0
  found = False

  while (i < len(numbers)):

    if numbers[i] == target:
      found = True
      break

    i = i + 1
  
  return found

print(linear_search([4, 7, 2, 9, 5], 1))
