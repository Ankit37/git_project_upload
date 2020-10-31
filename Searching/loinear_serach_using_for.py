list=[1,2,3,4,5,6,7,8,9]
n=5

def search(list,n):
    for i in list:
        if list[i]==n:
            return True
            i=i+1
        else:
            return False


if search(list, n):
    print("Found at :",)

else:
    print("Not found")
