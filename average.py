number_of_tests = 4
test1 = int(input("Score: "))
test2 = int(input("Score: "))
test3 = int(input("Score: "))
test4 = int(input("Score: "))

total = test1  +test2 + test3 + test4
average = total / number_of_tests

print(average)

if average > 69:
  print("You did it!")
else:
  print("Sorry, you didn't pass.")
