v, t = map(int, input().split())
s = v * t
print(s % 109 if s >= 0 else 109 - abs(s) % 109)