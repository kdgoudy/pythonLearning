temp = int(input("What is the temp today?: "))
print(temp)

if temp <= 60:
  print("It's cold outside")
elif temp <= 75:
  print("It feels nice outside")
elif temp <= 90:
  print("It's kind of warm outside")
else:
  print("It's hot outside")
