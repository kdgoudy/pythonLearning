#Determine if string is a palindrome
#ex. dad, mom, madam, rotor

org_string = input('Input a string: ')
reverse_string = org_string[::-1]
if org_string==reverse_string:
  print('The string is a palindrome')
else:
  print('Not a palindrome')
