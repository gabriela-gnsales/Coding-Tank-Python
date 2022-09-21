
for x in range(1, 30):
    if x % 2 == 0 and x % 10 == 0:
        print(x)  # comando1 = 10, 20
    if x % 3 == 0 and x % 4 == 0:
        print(x)  # comando2 = 12, 24
    if x % 3 == 0 and x % 11 == 0:
        print(x)  # comando3
    if x % 3 == 0:
        print(x)  # comando3 = 3, 6, 9, 12, 15, 18, 21, 24, 27
    if x % 11 == 0:
        print(x)  # comando3 = 11, 22


# resultado:
# 10
# 12
# 20
# 24
