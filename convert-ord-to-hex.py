import os

def ord2hex(string):
 result = ""
 for i in string:
  r = hex(ord(i));
  r = r.replace('0x','')
  result = result+r
 return '0x'+result

text="Helloword"
print(ord2hex(text))
