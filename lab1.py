def Linear_search(arr,n,k):
     for i in range(0,n):
         if k==arr[i]:
             return i
     return -1
arr=[]
n=int(input("Enter a Limit:"))
print("The array elements are:")
for i in range(0,n):
   arr.insert(i,input())
print (arr)
k=int(input("Enter a key element"))
r=Linear_search(arr,n,k)
if r == -1:
      print("The element not is found")
else:
      print("elemnt is  found at location",r)
