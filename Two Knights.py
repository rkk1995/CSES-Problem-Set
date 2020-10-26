# TIME LIMIT EXCEEDED

# Kind of a DP solution
# Find number of knights in i-1
# for I, add the outer L from the new col/row. Since only 2 can make a pair with each other in the same L, add # of cells in L - 2
# for rest, calculate if in any direction therse a valid point in the (i-1)(i-1) grid. If so remove it


# n = int(input())
# numKnights = 0
# directions = [[-2,-1],[-2,1],[-1,2],[-1,-2]]
# def isValidCoord(x,y,maxX,maxY):
#     if x >= 1 and y >= 1 and x <= maxX and y <= maxY:
#         return True
#     return False

# for i in range(1,n+1):
#     if i == 1:
#         print(0)
#     elif i ==2 :
#         numKnights = 6
#         print(numKnights)
#     else:
#         newCells = (2*i - 1)
#         newArrangementsFromNewColAndRow = newCells*(newCells - 1)/2 + (i-1)*(i-1)*newCells - 2
#         overCount = 0
#         for coord in [[i,x] for x in range(1,i)]:
#             for direction in directions:
#                 y,x = coord[0] + direction[0], coord[1] + direction[1]    
#                 if isValidCoord(x,y, i-1, i-1):
#                     overCount += 1
#         numKnights = numKnights + newArrangementsFromNewColAndRow - 2 * overCount - 2
#         print(int(numKnights))

# If two knight attack each other then they will be in 2*3 rectangle or 3*2 rectangle. 
# So the number of ways of placing them is (n-1)*(n-2)+(n-2)*(n-1). Also in each rectangle no ways of placing the knight is 2.
#  So total ways of placing knight so that they attack each other will be 2*2*(n-1)*(n-2).
#  So the number of ways such that knight do not attack each other will be n*n*(n*n-1)/2 — 4*(n-1)*(n-2)



n = int(input())

for k in range(1,n+1):
    totalCells = k*k
    totalCombos = totalCells * (totalCells - 1)/2
    if k>2:     
        totalCombos -= 4*(k-1)*(k-2)
    print(int(totalCombos))