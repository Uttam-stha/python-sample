# School Management System

students = {}
teachers = {}
courses = {}

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students[student_id] = {"name": name, "grade": grade}
    print("✅ Student added successfully!")

def add_teacher():
    teacher_id = input("Enter teacher ID: ")
    name = input("Enter teacher name: ")
    subject = input("Enter subject: ")
    teachers[teacher_id] = {"name": name, "subject": subject}
    print("✅ Teacher added successfully!")

def add_course(): 
    course_id = input("Enter course ID: ")
    title = input("Enter course title: ")
    teacher_id = input("Enter teacher ID for this course: ")
    if teacher_id in teachers:
        courses[course_id] = {"title": title, "teacher": teachers[teacher_id]['name']}
        print("✅ Course added successfully!")
    else:
        print("❌ Teacher ID not found.")

def view_students():
    if not students:
        print("📭 No students found.")
    else:
        print("\n📘 Students List:")
        for sid, info in students.items():
            print(f"ID: {sid}, Name: {info['name']}, Grade: {info['grade']}")

def view_teachers():
    if not teachers:
        print("📭 No teachers found.")
    else:
        print("\n📗 Teachers List:")
        for tid, info in teachers.items():
            print(f"ID: {tid}, Name: {info['name']}, Subject: {info['subject']}")

def view_courses():
    if not courses:
        print("📭 No courses found.")
    else:
        print("\n📙 Courses List:")
        for cid, info in courses.items():
            print(f"ID: {cid}, Title: {info['title']}, Teacher: {info['teacher']}")

def main():
    while True:
        print("\n🎓 --- School Management System ---")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. View Students")
        print("5. View Teachers")
        print("6. View Courses")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_teacher()
        elif choice == "3":
            add_course()
        elif choice == "4":
            view_students()
        elif choice == "5":
            view_teachers()
        elif choice == "6":
            view_courses()
        elif choice == "7":
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

main()