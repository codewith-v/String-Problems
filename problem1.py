#strings
#To check if given string is palindrome or not
#A palindrome reads same backwards
st=input("Enter the String: ")
if st[::-1]==st:
  print('Yes it is Palindrome')
else:
  print('Not a Palindrome')
