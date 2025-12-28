def main():
    m = int(input())
    
    
    course_data = {}
    
   
    student_data = {}
    
    for _ in range(m):
        course_line = input().split()
        course_code = course_line[0]
        semester_code = course_line[1]
        year = semester_code[:3]
        credit = int(course_code[3])
        n = int(course_line[2])
        
        for i in range(n):
            student_line = input().split()
            student_id = student_line[0]
            
            if student_line[1] == 'w':
                score = None  
            else:
                semester_score = int(student_line[1])
                if course_code[:3] in ['101', '201']:  
                    exam_score = int(student_line[2])
                   
                    score = int(semester_score * 0.7 + exam_score * 0.3)
                    if semester_score * 0.7 + exam_score * 0.3 > score:
                        score += 1
                else:
                    score = semester_score
            
            is_withdraw = score is None
            
           
            if (course_code, year) not in course_data:
                course_data[(course_code, year)] = []
            course_data[(course_code, year)].append((student_id, score, credit, is_withdraw))
            
           
            if student_id not in student_data:
                student_data[student_id] = {}
            if year not in student_data[student_id]:
                student_data[student_id][year] = []
            student_data[student_id][year].append((course_code, score, credit, is_withdraw))
    
    
    dept_entry_course_year = {}
    dept_entry_all_students = {}
    
    for student_id, years in student_data.items():
        entry_year = student_id[:3]
        dept = student_id[3:6]
        
        for course_year, courses in years.items():
          
            total_score_credit = 0
            total_credit = 0
            withdraw_count = 0
            total_courses = len(courses)
            
            for course_code, score, credit, is_withdraw in courses:
                if not is_withdraw:
                    total_score_credit += score * credit
                    total_credit += credit
                else:
                    withdraw_count += 1
            
            if total_credit > 0:
                annual_avg = total_score_credit // total_credit
            else:
                annual_avg = 0
            
            withdraw_percent = (withdraw_count * 100) // total_courses if total_courses > 0 else 0
            
            key = (dept, entry_year, course_year)
            if key not in dept_entry_all_students:
                dept_entry_all_students[key] = []
            dept_entry_all_students[key].append((student_id, annual_avg, withdraw_percent))
           
            if total_credit > 0 and annual_avg < 60:
                if key not in dept_entry_course_year:
                    dept_entry_course_year[key] = []
                dept_entry_course_year[key].append((student_id, annual_avg, withdraw_percent))
    

    for key in sorted(dept_entry_all_students.keys()):
        dept, entry_year, course_year = key
        total_all_students = len(dept_entry_all_students[key])
        
        if key in dept_entry_course_year:
            students = dept_entry_course_year[key]
            students.sort(key=lambda x: (-x[1], x[0]))
            total_students_less_60 = len(students)
        else:
            students = []
            total_students_less_60 = 0
        
        if total_students_less_60 < 3:
            print(f"{dept} {entry_year} {course_year}")
            print("Not Enough Student")
        else:
            print(f"{dept} {entry_year} {course_year}")
            
            all_students_sorted = sorted(dept_entry_all_students[key], key=lambda x: (-x[1], x[0]))
            
            for rank_in_less_60, (student_id, annual_avg, withdraw_percent) in enumerate(students[:3], 1):
                
                rank_in_all = all_students_sorted.index((student_id, annual_avg, withdraw_percent)) + 1
                
                percent = 1
                while True:
                    numerator = total_all_students * percent
                    if numerator % 100 == 0:
                        ceil_result = numerator // 100
                    else:
                        ceil_result = numerator // 100 + 1
                    
                    if ceil_result >= rank_in_all:
                        break
                    percent += 1
                
                print(f"{student_id} {annual_avg} {percent}% {withdraw_percent}%")
    
    
    course_year_data = {}
    
    for (course_code, year), students in course_data.items():
        valid_scores = [score for _, score, _, is_withdraw in students if not is_withdraw]
        
        if valid_scores:
            max_score = max(valid_scores)
            min_score = min(valid_scores)
            avg_score = sum(valid_scores) // len(valid_scores)
            
            total_students = len(students)
            withdraw_count = sum(1 for _, _, _, is_withdraw in students if is_withdraw)
            withdraw_percent = (withdraw_count * 100) // total_students
            
            above_40 = sum(1 for score in valid_scores if score > 40)
            
            course_year_data[(course_code, year)] = (max_score, avg_score, min_score, withdraw_percent, above_40)
    
    # 排序並輸出第二部分
    for (course_code, year) in sorted(course_year_data.keys()):
        max_s, avg_s, min_s, w_p, a40 = course_year_data[(course_code, year)]
        print(f"{course_code} {year}")
        print(f"{max_s} {avg_s} {min_s} {w_p}% {a40}")

if __name__ == "__main__":
    main()
