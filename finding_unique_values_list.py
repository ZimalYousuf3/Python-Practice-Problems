# Tracking Unique Numbers in a list

def count_unique(numbers):
  tracker = []
  for num in numbers:
    if num not in tracker:
      tracker.append(num)
      
  return len(tracker)

print(count_unique([5, 5, 5, 8, 9]))
