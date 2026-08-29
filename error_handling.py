b = 10

b = b - 10

try:
    c = 15 / b
except Exception as e:
    print(e)
    c = 0


d = input()

try:
    d = d + 10
except Exception as e:
    d = int(d) + 10

print(d)