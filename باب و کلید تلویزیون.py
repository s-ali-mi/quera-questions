values = input().split()
n, x, k = int(values[0]), int(values[1]), int(values[2])
shabakeha = [input() for i in range(n)]
print(shabakeha[((x+k)%n)-1])