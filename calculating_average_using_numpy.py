# Create a 2D array of 3 students × 3 subjects of scores; print each student's average (arr.mean(axis=1)

import numpy as np

scores = np.array([[78, 56, 33], [99, 87, 82], [78, 93, 86]])

print ('Array: ')
print(scores)
print('Shape: ', scores.shape)

avg = scores.mean(axis=1)
for i, a in enumerate(avg):
  print(f'Student-{i+1}: {a:.1f}')
