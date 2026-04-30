d = int(input("Enter total students: "))
for i in range (d):
    obt_marks = int(input("Enter your marks: "))
    t_marks = int(input("Enter your total marks: "))
    st_roll_no = int(input("Enter student roll no: "))
    st_name  = input("Enter student name: ")
    c = (obt_marks/t_marks)*100

    print("Name:",st_name)
    print("Roll No:",st_roll_no)
    print("Result:",c)

    if c >= 90:
        print("Grade: A")   
    elif c >= 85:
        print("Grade: A-")   
    elif c >= 80:
        print("Grade: B+")
    elif c >= 75:
        print("Grade: B")
    elif c >= 70:
        print("Grade: B-")
    elif c >= 65:
        print("Grade: C+")
    elif c >= 60:
        print("Grade: C")
    elif c >= 55:
        print("Grade: C-")
    elif c >= 50:
        print("Grade: D")

    else:
        print("Grade: F")
