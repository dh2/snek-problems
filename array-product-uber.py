# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers 
# in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Loop through array, keeping track of index and splicing out the data from the original then looping over the remaining list
def getProduct(l):
    x = 1
    for p in l:
        x = x * p
    
    return x

list1 = [1, 2, 3, 4, 5]
list2 = [3,2,1]

def do_product(l):
    product = []

    for idx,num in enumerate(l):
        temp = l[:]
        temp.pop(idx)
        product.insert(idx,getProduct(temp))

    print(product)

do_product(list1)
do_product(list2)
