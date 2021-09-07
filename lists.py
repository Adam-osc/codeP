courses = ['History', 'Math']

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ", ".join(courses)

new_list = course_str.split(", ")

print(course_str)
print(new_list)

