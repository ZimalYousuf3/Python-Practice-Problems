# count occurances

def count_occurrences(numbers, target):
    count = 0
    i = 0
    while i < len(numbers):
      if numbers[i] == target:
        count = count + 1
      i = i + 1
    return count

print(count_occurrences([3, 3, 3, 5], 3))
