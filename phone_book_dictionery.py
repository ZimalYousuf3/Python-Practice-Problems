# Build a phonebook dictionary (name → number) with at least 3 entries; let the user look up a name

name = input('Enter a name: ')
phone_book = [
    {'name' : 'Zimal', 'contact' : 3333762933},
    {'name' : 'Fajar', 'contact' : 3352749746},
    {'name' : 'Hooria', 'contact' : 3074920411}
]
for n in phone_book:
  if n['name'] == name:
    print(f'Name: {n['name']}, Contact: {n['contact']}')
    break
else:
    print('Name not found')
