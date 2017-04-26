from itertools import product, permutations, combinations, combinations_with_replacement, groupby
# itertools.product() computes the cartesian product of input iterables. 
# product(A, B) returns the same as ((x,y) for x in A for y in B)
a = [1,2,3]
b = [4,5,6]
cartesian_product_of_a_n_b = product(a,b)
# Prints (1, 4) (1, 5) (1, 6) (2, 4) (2, 5) (2, 6) (3, 4) (3, 5) (3, 6)
print(*cartesian_product_of_a_n_b)

# itertools.permutations(iterable[, r])  returns successive 'r' length permutations of elements in an iterable
# If 'r' is not specified or is None, then 'r' defaults to the length of the iterable, 
# and all possible full length permutations are generated.
# Prints [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
print(list(permutations(['1','2','3'],2)))
# Prints [('a', 'c'), ('a', 'b'), ('c', 'a'), ('c', 'b'), ('b', 'a'), ('b', 'c')]
print(list(permutations('acb',2)))

# itertools.combinations(iterable, r)  returns the r length subsequences of elements from the input iterable.
# Prints [('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]
print(list(combinations('1234',2)))

# itertools.combinations_with_replacement(iterable, r) returns r length subsequences of elements 
# from the input iterable allowing individual elements to be repeated more than once.
# Prints [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('2', '2'), ('2', '3'), ('2', '4'), ('3', '3'), ('3', '4'), ('4', '4')]
print(list(combinations_with_replacement('1234',2)))

# itertools.groupby returns consecutive keys and groups from the iterable. 
# It returns a iterable tuples (k, g) where k is key and g is iterable which can be a list again.
input_string = '1222311'
# Prints 1 ['1'] 2 ['2', '2', '2'] 3 ['3'] 1 ['1', '1'] 
for k, g in groupby(input_string):
    print(k, list(g), end=" ") # Here k is also string