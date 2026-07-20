csv_text = """name,region,sales
Zimal,North,250
Fajar,South
Zumar,East,180
Sukaina,,300
Hira,West,210"""

with open("sales.csv", "w") as f:
  f.write(csv_text)

import pandas as pd

df = pd.read_csv('sales.csv')
df

