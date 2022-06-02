# Q1

seq = []
while True:
    n = int(input())
    if (n > 0):
        seq.append(n)
    else:
        break

for i in seq[::-1]:
    print (i)
