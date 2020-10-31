
p=-1
def search(list,n):

 l=0;
 u=len(list)-1
 while l<=u:
     mid=(l+u)//2

     if list[mid]==n:
         globals()['p']=mid
         return True
     else:
         if list[mid]<n:
             l= mid+1
         else:
             u=mid-1
 return False


list=[11,22,33,44,55,66,77,88,99]
n=22

if search(list, n):
    print("Found at :",p+1)

else:
    print("Not found")
