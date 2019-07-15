h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())

print(s2 + 60 * (m2 + 60 * h2) - (s1 + 60 * (m1 + 60 * h1)))