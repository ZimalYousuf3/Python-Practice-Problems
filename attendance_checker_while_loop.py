# Attendence Checker

def is_present(students, name):
  i = 0
  found = False

  while (i < len(students)):

    if students[i] == name:
      found = True
      break

    i = i + 1
  
  return found

print(is_present(["Ali", "Sara", "Zimal"], "Zimal"))
