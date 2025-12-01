#Maps Is Basically To perform an operation like list or any iterable object

l = [1,2,3,4,5,6,7]

# print(map(lambda x : x*x*x ,l)) #It will give you map object you can typecast to get satisfied answer
# print(list(map(lambda x : x*x*x ,l)))

#Filter is like maps but it only takes value that function capable to take
# print(filter(lambda x : x>1 ,l))
# print(list(filter(lambda x : x>3 ,l)))

#Reduce Is Performs Operation On iterable objects

from functools import reduce
print(reduce(lambda x, y: x+y, l ))
