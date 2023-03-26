def selection_sort(a,n):
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]
    
a=[72, 50, 10, 44, 8, 20]
print('before sorting')
print(*a)
selection_sort(a,len(a))
print('after sorting')
print(*a)
