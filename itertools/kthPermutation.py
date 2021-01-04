from itertools import permutations

def kthPermutation(numbers, k):
    return list(permutations(numbers,len(numbers)))[k-1]
print("Test 1:",end=' ')
print(kthPermutation([1,2,3,4,5],4)==(1, 2, 4, 5, 3))
print("Test 2:",end=' ')
print(kthPermutation([11, 22, 31, 43, 56],120)==(56, 43, 31, 22, 11))
print("Test 3:",end=' ')
print(kthPermutation([1,2],1)==(1,2))