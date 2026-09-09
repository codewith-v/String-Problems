# To find the most frequent element in the string
s=input('enter string')
set_s=set(s)
m=None
for ch in set_s:
  if m==None:
    m=ch
  else:
    if s.count(ch)>=s.count(m):
      m=ch
print(m)
