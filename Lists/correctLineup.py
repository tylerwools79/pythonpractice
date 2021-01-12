def correctLineup(athletes):
    return [athletes[i^1] for i in range(len(athletes))]
print(correctLineup([1,2,3,4,5,6])==[2, 1, 4, 3, 6, 5])