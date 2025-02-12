rows = int(input("Enter Rows = "))

for i in range(0, rows, 1):
    for j in range(0, i):
        print('*', end = ' ')
    print()
