# Task no.5:
def cal_points(t_points , t_subjects):
    GPA=t_points/t_subjects
    return GPA

subjects=int(input("Enter your subjects:"))

t_grades=0
t_credit=0

for i in range(subjects):
    grades=float(input("Enter your points:"))
    credit=int(input("Enter your credit_hrs:"))

total_points = t_grades * t_credit

grades += total_points
t_credit += credit

GPA = (t_grades,t_credit)

print("semester gpa =",GPA)