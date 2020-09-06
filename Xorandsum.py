import os
import sys

#
# Complete the xorAndSum function below.
#
def xorAndSum(a, b):
        a=int(a,2)
        b=int(b,2)
        ans=0
        for i in range(0,314160):
                ans+=(a^(b<<i))
        return ans%(10**9 +7)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    result = xorAndSum(a, b)
    fptr.write(str(result) + '\n')
    fptr.close()  
