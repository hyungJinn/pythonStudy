import sys
input = sys.stdin.readline

X = int(input())
Y = int(input())

if (X > 0) & (Y > 0):
    print(1)
elif (X < 0) & (Y > 0):
    print(2)
elif (X < 0) & (Y < 0):
    print(3)
elif (X > 0) & (Y < 0):
    print(4)