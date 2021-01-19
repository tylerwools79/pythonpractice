#this function takes two lists, and removes any matching elements in both lists.
def groupDating(male, female):
    return [[x for x,y in zip(male,female) if x!=y],[y for x,y in zip(male,female) if x!=y]]
print(groupDating([1,2,3,4,5],[5,4,3,2,1])==[[1,2,4,5],[5,4,2,1]])
print(groupDating([5,28,14,99,17],[5,14,28,99,16])==[[28,14,17],[14,28,16]])
print(groupDating([42],[64])==[[42],[64]])
print(groupDating([1,2,3],[1,2,3])==[[],[]])