from itertools import dropwhile
# an exercise to demonstrate dropwhile.
#takes in a list of strings, returns the 3 strings after the first string of even length.
def memoryPills(pills):
    gen = dropwhile(lambda x: len(x)%2>0, pills+["","",""])
    next(gen)
    return [next(gen) for _ in range(3)]
	
print(memoryPills(["even"])==["","",""])
print(memoryPills(["Med 1", "Med 2", "Med 3", "Med 10", "Med 11", "Med 12", "Med 13", "Med 42", "Med 239"])==["Med 11","Med 12","Med 13"])