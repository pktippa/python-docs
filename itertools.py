from itertools import product, permutations
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