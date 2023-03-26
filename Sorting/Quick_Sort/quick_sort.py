def merge(a,low,high):
    pivot=a[high]
    idx=low-1
    for j in range(low,high):
        if a[j]<pivot:
            idx+=1
            a[idx],a[j]=a[j],a[idx]
    a[idx+1],a[high]=a[high],a[idx+1]
    return idx+1


def quick_sort(a,low,high):
    if low<high:
        pi=merge(a,low,high)
        quick_sort(a,low,pi-1)
        quick_sort(a,pi+1,high)


a=[12, 8, 4, 14, 36, 64, 15, 72, 67, 84]
print('before sorting')
print(*a)
quick_sort(a,0,len(a)-1)
print('after sorting')
print(*a)
