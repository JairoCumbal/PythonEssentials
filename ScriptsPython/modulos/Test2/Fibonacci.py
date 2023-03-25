"""
def Fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
        
    
Fibonacci(10)
"""

def Fibonacci(n):
    a, b = 0,1
    while a <= n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
        #a, b = b, a+b
        print()
Fibonacci(35)
