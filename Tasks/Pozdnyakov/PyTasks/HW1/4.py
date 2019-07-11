import os,pwd
print("Hello, ",pwd.getpwuid(os.getuid())[0],"!",sep='')
