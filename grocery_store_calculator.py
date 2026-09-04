# Grocery Store Calculator

def grocery_store():

  total_price = 0
  grocery = {}
  
  while True:
    item_name = input("\nEnter Item name (Press q/Q to quit): ")
    
    if item_name.upper() == 'Q':
      print(f'\nTHANK YOU FOR SHOPPING!')
      break
      
    item_price = input("Enter Item price (Press q/Q to quit): ")
    
    if item_price.upper() == 'Q':
      print(f'\nTHANK YOU FOR SHOPPING!')
      break
    
    item_price = float(item_price)
    total_price += item_price
    grocery[item_name] = item_price

  print(f"\n========= Receipt ==========\n")
  for names, prices in grocery.items():
    print(f'{names} - PKR {prices}')

  print(f"\nTotal Bill: PKR {total_price}\n")
  print(f"============================")

grocery_store()
