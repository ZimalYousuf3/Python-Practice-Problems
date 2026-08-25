# Tracking the most frequent number in a list

def most_frequent(numbers):
  count = {}
  for num in numbers:
    if num in count:
      count[num] = count[num] + 1
    else:
      count[num] = 1
  
  best_num = None
  best_count = 0

  for key, value in count.items():
    if value > best_count:
      best_num = key
      best_count = value
  
  return best_num

print(most_frequent([5, 1, 5, 8, 9]))
