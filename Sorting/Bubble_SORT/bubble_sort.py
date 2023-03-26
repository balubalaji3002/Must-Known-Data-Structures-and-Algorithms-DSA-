class bubble_sort:
    def b_sort(self,a,n):
        for i in range(0,n-1):
            for j in range(0,n-i-1,1):
                if a[j]>a[j+1]:
                    a[j+1],a[j]=a[j],a[j+1]


a=[64, 34, 25, 12, 22, 11, 90]
print('before sorting')
print(*a)
ob=bubble_sort()
ob.b_sort(a,len(a))
print('after sorting')
print(*a)
