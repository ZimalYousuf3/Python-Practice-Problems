# Getting scores from user
def get_scores():
  scores = []

  while True:
    entry = float(input('Enter your score or type "done" to stop:'))

    if entry == 'done':
      break
    scores.append(entry)
  return scores

# Calculating Average
def average(score):
  if len(score) == 0:
    return 0
  return sum(score)/len(score)

# Calculating Grade
def grade(score):
  if score >= 90:
    return 'A'

  elif score >= 75:
    return 'B'

  elif score >= 60:
    return 'C'

  elif score >= 45:
    return 'D'

  else:
    return 'F'

# Calculating Top Score
def top_score(score):
  top = scores[0]

  for score in scores:
    if score > top:
      top = scores
  return top

# Calculating No. passed students
def passed(score):
  count = 0

  for score in scores:
    if score >= 40:
      count = count + 1
  return count

# Main Program
score = get_scores()
print (score)

avg = average(score)
print (f'Average: {avg:.2f}')

topper = top_score(score)
print (f'Top Score: {topper}')

gr = grade(avg)
print (f'Grade: {gr}')

passed_students = passed(score)
print (f'Passed Students: {passed_students}')

