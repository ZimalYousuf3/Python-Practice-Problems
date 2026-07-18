# Write a program that reads students.csv and prints only students who scored above 90 — wrapped in try/except.

import csv

with open('students.csv', 'w', newline = '') as f:
  writer = csv.writer(f)
  writer.writerow(['name','score'])
  writer.writerow(['Zimal', 99])
  writer.writerow(['Fajar', 93])
  writer.writerow(['Maira', 80])
  writer.writerow(['Hooria', 67])
  writer.writerow(['Sara', 34])

try:
  with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
      if int(row[1]) > 90:
        print (row)

except FileNotFoundError:
    print('File not found')
