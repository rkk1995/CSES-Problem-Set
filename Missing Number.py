n = int(input())
nums = map(int,input().split())

total = (n)*(1+n)/2
for num in nums:
    total -= num

print(total)