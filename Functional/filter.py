def collegeCourses(x, courses): #a simple function that takes in a list and removes all elements of that list with x characters
    def shouldConsider(course):
        return len(course) != x

    return filter(shouldConsider, courses)