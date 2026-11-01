students = {}

def add_student(sid, name, marks):
    if sid in students:
        return False
    if len(marks) == 0:
        return False
    for m in marks:
        if m < 0 or m > 100:
            return False
    students[sid] = {'name': name, 'marks': marks}
    return True

def calculate_total(marks):
    total = 0
    for m in marks:
        total = total + m
    return total

def calculate_average(marks):
    total = calculate_total(marks)
    avg = total / len(marks)
    return avg

def get_grade(average):
    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Division"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"

def build_report(sid):
    data = students[sid]
    total = calculate_total(data['marks'])
    avg = calculate_average(data['marks'])
    grade = get_grade(avg)
    return {'total': total, 'average': avg, 'grade': grade}

def get_top_students(records):
    def avg_calc(sid):
        return calculate_average(records[sid]['marks'])
    
    filtered = list(filter(lambda x: avg_calc(x) >= 75, records))
    names = list(map(lambda x: records[x]['name'], filtered))
    return names

def class_avg(*args):
    s = 0
    for n in args:
        s = s + n
    return s / len(args)

def summary(**kwargs):
    title = kwargs.get('title', 'Class Report')
    passing = kwargs.get('passing_mark', 40)
    print(title)
    print("Passing mark:", passing)

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)
    
count = 0

n = int(input("How many students: "))
for i in range(n):
    sid = input("Student ID: ")
    name = input("Name: ")
    m1 = int(input("Mark 1: "))
    m2 = int(input("Mark 2: "))
    m3 = int(input("Mark 3: "))
    marks = [m1, m2, m3]
    
    
    add_student(sid, name, marks)


print(summary(title="Class Report", passing_mark=40))


print("\n===== STUDENT PERFORMANCE REPORT =====")
for sid in students:
    r = build_report(sid)
    print(f"{sid} | {students[sid]['name']} | Marks: {students[sid]['marks']}")
    print(f"Total: {r['total']} | Average: {r['average']:.2f} | Grade: {r['grade']}")
    print()


top = get_top_students(students)
print("High performers (average >= 75):", top)


all_avgs = []
for sid in students:
    all_avgs.append(calculate_average(students[sid]['marks']))

if len(all_avgs) > 0:
    print("Class average:", class_avg(*all_avgs))


print("Recursive sum from 1 to 5:", recursive_sum(5))
print("Recursive sum from 1 to 3:", recursive_sum(3))
print("Recursive sum from 1 to 4:", recursive_sum(4))
