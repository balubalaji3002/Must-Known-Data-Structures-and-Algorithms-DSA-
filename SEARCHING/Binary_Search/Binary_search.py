class search:
    def find(self,a,item):
        left=0
        right=len(a)-1
        while left<=right:
            mid=(left+right)//2
            if a[mid]==item:
                print('Item is found at index:',mid)
                return
            elif a[mid]>item:
                right=mid-1
            else:
                left=mid+1
        print("Item is not present in the array")

ob=search()
a=[10, 20, 30, 40, 50, 60, 70, 80]
item=10
ob.find(a,item)
