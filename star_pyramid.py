# Type 1 -->
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 

n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end="")
    for j in range(i+1):
        print("*",end =" ")
    
    print()

## other pyramid type-->
#    *
#   ***
#  *****
# *******

num = int(input('enter the num'))
cnt = num//2
# print(cnt)
scnt = 1

for i in range(cnt +1):
    print(cnt*" " + "*"*scnt)
    cnt = cnt-1
    scnt = scnt + 2
