import math

print("10 + 4 =", 10 + 4)
print("4 - 23 =", 5 - 23)
print("18 * 3600000.0 =", 18 * 3600000.0)
print("3 / 5 =", 3 / 5)
print("3 // 5 =", 3 // 5) # integer result
print("3 module 5 =", 3 % 5)
print("pow(2, 4) =", 2 ** 4) # pow(2, 4)

x = 5
x = x + 3
x += 3

y = 3
y *= 3

z = 10
z -= 5

print("x + y * z =", x + y * z)

print("10 + 3 * 2 ** 2 = ", 10 + 3 * 2 ** 2) # <=> pow(2, 2) * 3 + 10

print("(10 + 3) * 2 ** 2 =", (10 + 3) * 2 ** 2) # <=> pow(2, 2) * 13 => parentheses make priority

print("round(3.9) =", round(3.9))
print("round(3.4) =", round(3.4))
print("round(3.5) =", round(3.5))

print("abs(-3) =", abs(-3))

print("math.fabs(-2.9) =", math.fabs(-2.9))
print("math.pow(2, 6) =", math.pow(2, 6)) # 2 ** 6
print("math.ceil(2.9) =", math.ceil(2.9))
print("math.floor(2.9) =", math.floor(2.9))
print("math.factorial(5) =", math.factorial(5))
print("math.sqrt(9.0) =", math.sqrt(9.0))
print("math.gcd(10, 4) =", math.gcd(10, 4))
print("math.lcm(10, 9) =", math.lcm(10, 9))
print("math.sin(90.0) =", math.sin(90.0))
print("math.cos(0.0) =", math.cos(0.0))
print("math.log(8, 2) =", math.log(8, 2))
print("math.log10(1000) =", math.log10(1000)) # math.log(1000, 10)
print("math.log2(8) =", math.log2(8)) # math.log(8, 2)
print("math.degrees(math.pi * 2) =", math.degrees(math.pi * 2))
print("math.radians(180.0) =", math.radians(180.0))
