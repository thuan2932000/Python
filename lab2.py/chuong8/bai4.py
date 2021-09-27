ids =[4353, 2314, 2956, 3382, 9362, 3900]
#cau a. 
ids.remove(3382)
print(ids)
#cau b. 
ids.index(9362)
print(ids)
#cau c. 
ids.insert(ids.index(9362) + 1, 4499)
print(ids)
#cau d. 
ids = ids + [5566, 1830]
print(ids)
#cau e. 
ids.reverse()
print(ids)
#cau f. 
ids.sort()
print(ids)