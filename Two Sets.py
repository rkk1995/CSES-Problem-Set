# Logic here is that sum of 1 - n  = (n+1)(n)/2
# Therefore each set has to be equal to (n+1)(n)/4
# Remove the case where sum of 1-n is not divisible by 2
# Now this leaves each set to be equal to S = (n+1)(n)/4
# S can only be divisible by either (n+1) or (n)
# If S is divisible by n+1 , then we can make N/4 groups of N+1, ex  N = 8. S = 18 divisible by n+1 so we can make N/4 = 2 groups of 9. done by (1,8,2,7)
#                                                                               Other group is (3,6,4,5)
# If S is divisible by n, then we can make (n+1)/4 groups of N, ex N=7 S = 14 divisible by n so we can make (N+1)/4 = 8/4 = 2 groups of 7. done by (7,1,6) and (2,5,3,4)

n = int(input())

if ((n*(n+1))/2) %2 != 0:
    print("NO")
else: 
    L1 = []
    L2 = []

    halfSum = (n*(n+1)/4)

    l = 1
    r = n
    if halfSum%n == 0:
        L1.append(n)
        r -= 1
        for _ in range(int((n+1)/4) - 1):
            L1.append(l)
            L1.append(r)
            r -= 1
            l += 1
    else: 
        for _ in range(int(n/4)):
            L1.append(l)
            L1.append(r)
            r -= 1
            l += 1

    print("YES")
    print(len(L1))
    for ele in L1:
        print(ele, end=" ")

    print("\n")
    print(r-l+1)
    for i in range(l,r+1):
        print(i, end =" ")
            

