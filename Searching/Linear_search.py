
p=0
def search(list,n):
    i=0
    while i< len(list):
      if   list[i]==n:
       globals() ['p']=i
       return True
      i=i+1
    return False


list=[1,2,3,4,5,6,7,8,9]
n=5

if search(list, n):
    print("Found at :",p+1)

else:
    print("Not found")
