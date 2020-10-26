n = int(input())
answer = 1

for i in range(n):
    answer = 2*answer%((10**9)+7)

print(answer)



