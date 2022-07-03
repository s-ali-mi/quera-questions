n = int(input())
a = [int(input()) for i in range(n)]
EndInterval = 0
for i in range(0, n):
    for j in range(i+1, n):
        EndInterval += a[i] * a[j]

for i in range(153, EndInterval*2):
    h = 0
    if h < i:
        for j in str(i):
            h += int(j)**len(str(i))
            if h > i: break
        if i == h:
            print(i)