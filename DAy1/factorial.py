

def fact(f):
    c=1
    for i in range(1,f+1):
        c=c*i

    return c


def fact_rec(n):

    if n==0:
     return 1
    return n* fact_rec(n-1)

result=fact_rec(4)


print(result)