

def sum(*b):
    c=0
    for i in b:
        c=c+i

    print(c)

def info(name, **data):

    print(name)
    for i,j in data.items():
        print(i,":",j)

sum(2,3,4,5)
info(name='Ankit', age=25, mobile=443434)