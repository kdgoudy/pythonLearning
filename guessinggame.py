secret_word = "wolf"
guess = ""

#while loop to keep the game going if you guess incorrectly
while guess != secret_word:
  guess = input("Enter guess: ")
  
print("You win!")
