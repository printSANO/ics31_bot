from canvasapi import Canvas
from to import s_key, url

#University of California Irvine
canvas_url = url
#Access token
canvas_key = s_key
#initialize
canvas = Canvas(canvas_url, canvas_key)

def course_name(num: int):
    name = canvas.get_course(num)
    return str(name)

def assingment_id_extractor(course_num: int) -> list:
    course = canvas.get_course(course_num)
    assignments = course.get_assignments()
    assign_ids = []
    assign_ids.append(course_num)
    for i in assignments:
        assign_ids.append(i)
    return assign_ids

def get_due_dates(assignment_ids: list) -> dict:
    assigned = {}
    for j in range(1,len(assignment_ids)):
        assignment = assignment_ids[j]
        due_date = str(assignment.due_at_date)[0:-9]
        assignment_name = str(assignment.name)
        assigned[str(assignment_name)] = due_date
    return assigned

if __name__ == "__main__":
    num = 48939
    print(course_name(num))
    test = assingment_id_extractor(num)
    test1 = get_due_dates(test)
    print(test1)