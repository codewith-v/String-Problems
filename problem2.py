#2 To check if s1 is reverse of s2 
s1=input('Enter string 1:')
s2=input('Enter string 2:')
if s1==s2[::-1]:
  print('s1 is reverse of s2')
else:
  print('s1 is not reverse of s2')
