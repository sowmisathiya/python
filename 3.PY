import sys
vow='aeiouAEIOU'
d='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
c=input()
if c in vow:
  print('Vowel')
elif c in d:
  print('Consonant')
else:
  print('invalid')
