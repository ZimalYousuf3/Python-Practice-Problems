# Greeting according to time

import time

time_stamp = time.strftime('%H:%M:%S')

if time_stamp >= "00:00:00" and time_stamp < "12:00:00":
  print("Good Morning!")

elif time_stamp >= "12:00:00" and time_stamp < "17:00:00":
  print("Good Afternoon!")

elif time_stamp >= "17:00:00" and time_stamp < "19:00:00":
  print("Good Evening!")

else:
  print("Good Night")
