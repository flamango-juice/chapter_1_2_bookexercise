import math

# Exercise 1
n = 17
# 17 = n - SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
x = y = 1
print(x,y)#; - Trailing semicolon in the statement
print(x,y)#. SyntaxError: invalid syntax

#Exercise 2, p1
radius = 3
vol = (4 / 3) * math.pi * radius ** 3
print(f"""
Radius: {radius} cm
Volume: {vol:.0f} cubic cm
""")

#p2
g = 42

coss = math.cos(g) ** 2
sinn = math.sin(g) ** 2

print(f"""
x = {g}
cos x^2: {coss:.5f}
sin x^2: {sinn:.5f}
sum: {sinn + coss:.5f}
""")

#p3
print(math.e ** 2)
print(pow(math.e,2))
print(math.exp(2))