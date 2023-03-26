class search:
    def find(self,a,item):
        for i in range(len(a)):
            if a[i]==item:
                print("item Found at index:",i)
                return
        print("Item is not present in the array")
        return
ob=search()
a=[12, 5, 18, 25, -3, 19]
item=25
ob.find(a,item)
