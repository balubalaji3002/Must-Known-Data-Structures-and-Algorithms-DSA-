def merge(a,low,mid,high):
    n1=mid-low+1
    n2=high-mid
    left_a=[0]*(n1)
    right_a=[0]*(n2)
    k=low
    for i in range(0,n1):
        left_a[i]=a[low+i]
    for j in range(0,n2):
        right_a[j]=a[mid+1+j]
    i=j=0
    while i<n1 and j<n2:
        if left_a[i]<right_a[j]:
            a[k]=left_a[i]
            i+=1
        else:
            a[k]=right_a[j]
            j+=1
        k+=1
    
    while i<n1:
        a[k]=left_a[i]
        i+=1
        k+=1
    while j<n2:
        a[k]=right_a[j]
        j+=1
        k+=1

def merge_sort(a,low,high):
    if low<high:
        mid=(low+high)//2
        merge_sort(a,low,mid)
        merge_sort(a,mid+1,high)
        merge(a,low,mid,high)
    
a=[12, 8, 4, 14, 36, 64, 15, 72, 67, 84]
print('before sorting')
print(*a)
merge_sort(a,0,len(a)-1)
print('after sorting')
print(*a)
