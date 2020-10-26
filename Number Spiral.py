

## Approach finds the max value of (maxIndex-1)**2 and then traverses on the next loop based on which coordinate is the max 
n = int(input())

def isEven(x):
    return x%2 == 0

def isOdd(x):
    return x%2 == 1

for test in range(n):
    y,x = input().split()
    y = int(y)
    x = int(x)
    mxIndex = max(x,y)
    prevMax = (mxIndex-1)**2
    ans = 0

    if (mxIndex%2 == 0):
        if (x==mxIndex):
            ans = prevMax + y
        else:
            ans = prevMax + (2*mxIndex-1) - (x-1)
    else:
        if (y==mxIndex):
            ans = prevMax + x 
        else:
            ans = prevMax + (2*mxIndex-1) - (y-1)
    print(ans)


# Finds the corner of the maxIndex and then calculates offset from there based on which coordinate == maxIndex

# def f(a, b): 
#     M = max(a, b) 
#     return(a-b)*(-1)**M+M*M-M+1

# N = int(input())
# for _ in range(N):
#     y,x = input().split()
#     x = int(x)
#     y = int(y)
#     M = max(y,x)
#     corner = M*M - M + 1
#     diff = (y-x)
#     corner += diff*(-1)**M

#     print(corner)
