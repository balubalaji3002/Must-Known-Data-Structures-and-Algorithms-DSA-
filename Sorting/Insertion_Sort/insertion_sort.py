def insertion_sort(a,n):
    for i in range(1,n):
        j=i-1
        key=a[i] 
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    
a=[64, 34, 25, 12, 22, 11, 90]
print('before sorting')
print(*a)
insertion_sort(a,len(a))
print('after sorting')
print(*a)
