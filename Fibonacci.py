n = int(input("Enter the number of Fibonacci terms: "))
a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b  # Update values
