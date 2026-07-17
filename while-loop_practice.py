# Write a program that keeps asking the user for numbers until they type "done", then prints the total and count

total = 0
count = 0

while True:
  user_input = input("Enter a number  (enter done to finish): ")
  if user_input == 'done':
    print(f'done entered, Loop is finished')
    break
  num = float(user_input)
  total = total + num
  count = count + 1

print(f'Total:', total)
print(f'Count:', count)
