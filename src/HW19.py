def match(section1: str, section2: str, sections: list):
    if section1==section2:
        sections.append(section1)

def isConflict(course1:list, course2: list):
    result = []
    sections = []
    for i in range(course1[1]):
        for j in range(course2[1]):
            match(course1[2+i], course2[2+j], sections)
    if len(sections)>0:
        sections = sorted(sections)
        #c_ids = sorted([course1[0], course2[0]])
        c_ids = [course1[0], course2[0]]
        result = [c_ids, sections]
    return (result)
def printResult(result):
    if len(result[1]) > 1:
        for i in range(len(result[1])):
            print(f'{result[0][0]},{result[0][1]},{result[1][i]}')
    else:
        print(f'{result[0][0]},{result[0][1]},{result[1][0]}')


def getData():
    course = ['',0,'','','']
    course[0] = input() # course id
    course[1] = int(input()) #course hours
    for i in range(course[1]):
        day = []
        course[i+2] = input() # course sections
        for c in course[i+2]:
            if c.isdigit():
                day.append(int(c))
            else:
                day.append(c)
        if day[0] > 5:
            print('-1')
            exit()
    return course
def compute():
    n = int(input()) # number of courses
    courses = []
    for i in range(n):
        courses.append(getData())
    results = []
    for i in range(n-1): # 3 0 1 2
        for j in range(n-i-1): # 2 1 0 1 0
            result = isConflict(courses[i], courses[j+i+1])
            if result != []:
                results.append(result)
    #results = sorted(results)
    if len(results) == 0:
        print('correct')
    else:
        for i in range(len(results)):
            printResult(results[i])
compute()