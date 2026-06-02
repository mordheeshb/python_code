# Number Pattern Programs

# 1. Half Pyramid Pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\n" + "-" * 20)

# 2. Inverted Half Pyramid Pattern
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\n" + "-" * 20)

# 3. Repeated Number Pyramid
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

print("\n" + "-" * 20)

# 4. Inverted Repeated Number Pyramid
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

print("\n" + "-" * 20)

# 5. Floyd's Triangle
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("\n" + "-" * 20)

# 6. Reverse Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

print("\n" + "-" * 20)

# 7. Right Shifted Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(i, n + 1):
        print(j, end="")
    print()

print("\n" + "-" * 20)

# 8. Palindrome Number Pyramid
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

print("\n" + "-" * 20)

# 9. Continuous Number Triangle
n = 4
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("\n" + "-" * 20)

# 10. Binary Number Pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((i + j + 1) % 2, end="")
    print()
