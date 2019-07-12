import os,pwd
def Luke_I_am_your_father():
  print(pwd.getpwuid(os.getuid())[0],", I'm your father!",sep='')

print("Hello, ",input(),"!",sep='')
Luke_I_am_your_father()
