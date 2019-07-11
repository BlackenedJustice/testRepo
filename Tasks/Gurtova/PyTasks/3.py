n = int(input())
hour = n//60
minute = n - hour*60
hour = hour%24
print(hour, minute)
