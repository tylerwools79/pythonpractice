#this function takes a list and returns a list of sorted indexes where the 'i'th element's value [in participants] is less than 'i'
def checkParticipants(participants):
    return [x for x, y in enumerate(participants) if y < x]
print(checkParticipants([0,1,1,5,4,8])==[2])
print(checkParticipants([0,1,2,3,4,5])==[])
print(checkParticipants([3,3,3,3,3,3,3])==[4,5,6])
