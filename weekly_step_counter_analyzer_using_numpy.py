# Weekly Step-Count Analyzer

import numpy as np

step_count = np.array([5200, 8100, 7600, 4300, 9800, 12400, 6700])
total = step_count.sum()
average = step_count.mean()
best = step_count.max()
worst = step_count.min()

print('---------------------------------------------------------')
print('             Weekly Step-Count Analyzer')
print('---------------------------------------------------------')
print (f'Total Steps in a week: {total} steps')
print(f'Average Steps in a day: {average:.1f}' )
print(f'Best Day: {best} steps')
print(f'Worst Day: {worst} steps')
print('')
print('Steps in Weekdays:')

for i, row in enumerate(step_count[0:5]):
  print(f'Day-{i+1}: {row} steps')

print('')
print('Steps on Weekends:')

for i, row in enumerate(step_count[5:]):
  print(f'Day-{i+6}: {row} steps')

print('')
print(f'Wednesday count: {step_count[2]} steps')

print('')
print(f'Corrected Step Count (Tracker undercounted by 300) :')
corrected_steps = step_count + 300

for i, row in enumerate(corrected_steps):
  print(f'Day-{i+1}: {row} steps')

print('')
print(f'Steps into Kilometers:-')

for i, row in enumerate(corrected_steps):
  print(f'Day-{i+1}: {row/1300:.1f} km') # 1km = 1300 steps
print('')

combined_counter = np.array([[5200, 8100, 7600, 4300, 9800, 12400, 6700],[6100, 5900, 8800, 7200, 4000, 11000, 9500]])

print('COMBINED COUNTER:')
print(f'Shape:- {combined_counter.shape}')
print(combined_counter)
print('')

print(f'Weekly Total:-')
weekly_total = combined_counter.sum(axis=1)
for i, t in enumerate(weekly_total):
  print(f'Person-{i+1}: {t} steps')

print('---------------------------------------------------------')
