# Tracking how many times a number appears in a list

def count_once(numbers):
  tracker = []
  for num in numbers:
    if num not in tracker:
      tracker.append(num)
    else:
      tracker.remove(num)

  return len(tracker)

print(count_once([5, 1, 5, 8, 9]))
