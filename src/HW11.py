courses = []
conflicts = [] 
isConflict = False

for _ in range(3):
    course = int(input())
    time1 = int(input())
    time2 = int(input())
    
    courses.append({"id" :course, 
                    "time" : [int(time1), int(time2)]
                })




for i in range(3):
    course_A = courses[i]
    for j in range(i + 1, 3):  
        course_B = courses[j]
        for time_A in course_A["time"]:
            for time_B in course_B["time"]:
                if time_A == time_B:
                    isConflict = True

                    id1 = min(course_A["id"], course_B["id"])
                    id2 = max(course_A["id"], course_B["id"])

                    conflicts.append((id1, id2, time_A))
conflicts.sort() 

if isConflict == False:
    print("correct")
else:
    for id1, id2, time in conflicts:
        print(f"{id1} and {id2} conflict on {time}")
