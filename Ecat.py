import time

#Questions data
questions = []

questions.append({
    "subject": "Computer",
    "question": "Which component is responsible for executing instructions and processing data in a computer system?",
    "A": "RAM",
    "B": "CPU",
    "C": "GPU",
    "D": "Hard Drive",
    "answer": "B"
})

questions.append({
    "subject": "Mathematics",
    "question": "What is the value of 2x + 5 if x = 3?",
    "A": "8",
    "B": "10",
    "C": "11",
    "D": "13",
    "answer": "C"
})

questions.append({
    "subject": "Physics",
    "question": "What is the SI unit of force?",
    "A": "Joule",
    "B": "Newton",
    "C": "Watt",
    "D": "Pascal",
    "answer": "B"
})

questions.append({
    "subject": "Chemistry",
    "question": "What is the chemical symbol of Sodium?",
    "A": "So",
    "B": "Sd",
    "C": "Na",
    "D": "N",
    "answer": "C"
})

questions.append({
    "subject": "English",
    "question": "Choose the correct synonym of 'Rapid'.",
    "A": "Slow",
    "B": "Quick",
    "C": "Weak",
    "D": "Late",
    "answer": "B"
})

questions.append({
    "subject": "Mathematics",
    "question": "What is the derivative of x squared?",
    "A": "x",
    "B": "2x",
    "C": "x squared",
    "D": "2",
    "answer": "B"
})

questions.append({
    "subject": "Physics",
    "question": "Which quantity is measured in volts?",
    "A": "Current",
    "B": "Resistance",
    "C": "Potential difference",
    "D": "Power",
    "answer": "C"
})

questions.append({
    "subject": "Chemistry",
    "question": "Which gas is released during photosynthesis?",
    "A": "Oxygen",
    "B": "Carbon dioxide",
    "C": "Nitrogen",
    "D": "Hydrogen",
    "answer": "A"
})

questions.append({
    "subject": "Computer",
    "question": "Which of the following is an input device?",
    "A": "Monitor",
    "B": "Printer",
    "C": "Keyboard",
    "D": "Speaker",
    "answer": "C"
})

questions.append({
    "subject": "English",
    "question": "Choose the correct antonym of 'Ancient'.",
    "A": "Old",
    "B": "Modern",
    "C": "Past",
    "D": "Historic",
    "answer": "B"
})

answered_questions = {}
skipped_questions = []
student_marks = {}
student_results = []

admin_username = "ecat_admin"
admin_password = "ecat@2026"
student_username = "student"
student_password = "student123"

#Common functions
def empty_check(text):
    if text.strip() == "":
        return True
    else:
        return False

def calculate_grade(percentage):
    if percentage >= 80:
        return "EXCELLENT"
    elif percentage >= 65:
        return "GOOD"
    elif percentage >= 50:
        return "AVERAGE"
    else:
        return "BELOW AVERAGE"

def input_question_number(total_questions):
    number = input("Enter question number: ")
    if number.isdigit():
        number = int(number)
        if number >= 1 and number <= total_questions:
            return number
        else:
            print("Invalid question number.")
            return 0
    else:
        print("Invalid input. Enter number only.")
        return 0

#Admin functions
def admin_login():
    attempts = 0
    while attempts < 3:
        User = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if User == admin_username and password == admin_password:
            print("Welcome, Admin!")
            return True
        else:
            attempts = attempts + 1
            print("Invalid login. Attempts left:", 3 - attempts)
    print("Admin account locked due to 3 wrong attempts.")
    return False

def add_question(questions_list):
    subject = input("Enter subject: ")
    question_text = input("Enter the question: ")
    option_a = input("Enter option A: ")
    option_b = input("Enter option B: ")
    option_c = input("Enter option C: ")
    option_d = input("Enter option D: ")
    correct_answer = input("Enter the correct answer (A, B, C, or D): ").upper()

    if empty_check(subject) or empty_check(question_text) or empty_check(option_a) or empty_check(option_b) or empty_check(option_c) or empty_check(option_d):
        print("Empty input is not allowed.")
        return

    if correct_answer not in ["A", "B", "C", "D"]:
        print("Invalid answer. Please enter A, B, C, or D.")
        return

    new_question = {
        "subject": subject,
        "question": question_text,
        "A": option_a,
        "B": option_b,
        "C": option_c,
        "D": option_d,
        "answer": correct_answer
    }
    questions_list.append(new_question)
    print("Question added successfully!")

def view_questions(questions_list):
    if len(questions_list) == 0:
        print("No questions available.")
    else:
        question_number = 1
        for question in questions_list:
            print("----------------------------------------")
            print("Question No:", question_number)
            print("Subject:", question["subject"])
            print(question["question"])
            print("A. " + question["A"])
            print("B. " + question["B"])
            print("C. " + question["C"])
            print("D. " + question["D"])
            print("Correct Answer:", question["answer"])
            question_number = question_number + 1

def delete_question(questions_list):
    if len(questions_list) == 0:
        print("No questions available to delete.")
        return
    view_questions(questions_list)
    question_number = input_question_number(len(questions_list))
    if question_number != 0:
        del questions_list[question_number - 1]
        print("Question deleted successfully!")

def update_question(questions_list):
    if len(questions_list) == 0:
        print("No questions available to update.")
        return
    view_questions(questions_list)
    question_number = input_question_number(len(questions_list))
    if question_number != 0:
        subject = input("Enter new subject: ")
        question_text = input("Enter the new question: ")
        option_a = input("Enter new option A: ")
        option_b = input("Enter new option B: ")
        option_c = input("Enter new option C: ")
        option_d = input("Enter new option D: ")
        correct_answer = input("Enter the new correct answer (A, B, C, or D): ").upper()

        if empty_check(subject) or empty_check(question_text) or empty_check(option_a) or empty_check(option_b) or empty_check(option_c) or empty_check(option_d):
            print("Empty input is not allowed.")
            return

        if correct_answer not in ["A", "B", "C", "D"]:
            print("Invalid answer. Please enter A, B, C, or D.")
            return

        questions_list[question_number - 1] = {
            "subject": subject,
            "question": question_text,
            "A": option_a,
            "B": option_b,
            "C": option_c,
            "D": option_d,
            "answer": correct_answer
        }
        print("Question updated successfully!")

def question_bank_statistics(questions_list):
    print("Question Bank Statistics")
    print("Total Questions:", len(questions_list))
    subject_count = {}
    for question in questions_list:
        subject = question["subject"]
        if subject in subject_count:
            subject_count[subject] = subject_count[subject] + 1
        else:
            subject_count[subject] = 1
    for subject in subject_count:
        print(subject + ":", subject_count[subject])

def view_all_student_results():
    if len(student_results) == 0:
        print("No student results available.")
    else:
        count = 1
        for result in student_results:
            print("----------------------------------------")
            print("Result No:", count)
            print("Name:", result["name"])
            print("Roll Number:", result["roll_number"])
            print("Date/Time:", result["date_time"])
            print("Score:", result["score"])
            print("Percentage:", str(result["percentage"]) + "%")
            print("Grade:", result["grade"])
            count = count + 1

def view_detailed_result_per_student():
    if len(student_results) == 0:
        print("No student results available.")
        return
    roll_number = input("Enter roll number to view detailed result: ")
    if empty_check(roll_number):
        print("Roll number cannot be empty.")
        return
    found = False
    for result in student_results:
        if result["roll_number"] == roll_number:
            found = True
            print_student_result(result)
            review_answers(result)
    if found == False:
        print("No result found for this roll number.")

def class_result_statistics():
    if len(student_results) == 0:
        print("No student results available.")
        return

    highest_marks = student_results[0]["score"]
    lowest_marks = student_results[0]["score"]
    total_marks = 0
    pass_count = 0
    fail_count = 0
    excellent_count = 0
    good_count = 0
    average_count = 0
    below_average_count = 0

    for result in student_results:
        marks = result["score"]
        total_marks = total_marks + marks
        if marks > highest_marks:
            highest_marks = marks
        if marks < lowest_marks:
            lowest_marks = marks
        if result["percentage"] >= 50:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

        if result["grade"] == "EXCELLENT":
            excellent_count = excellent_count + 1
        elif result["grade"] == "GOOD":
            good_count = good_count + 1
        elif result["grade"] == "AVERAGE":
            average_count = average_count + 1
        else:
            below_average_count = below_average_count + 1

    average_marks = total_marks / len(student_results)
    print("Class Result Statistics")
    print("Highest Marks:", highest_marks)
    print("Lowest Marks:", lowest_marks)
    print("Average Marks:", round(average_marks, 2))
    print("Pass Count:", pass_count)
    print("Fail Count:", fail_count)
    print("Grade Distribution")
    print("EXCELLENT:", excellent_count)
    print("GOOD:", good_count)
    print("AVERAGE:", average_count)
    print("BELOW AVERAGE:", below_average_count)

#Student functions
def student_login():
    attempts = 0
    while attempts < 3:
        User = input("Enter student username: ")
        password = input("Enter student password: ")
        if User == student_username and password == student_password:
            print("Welcome, Student!")
            return True
        else:
            attempts = attempts + 1
            print("Invalid login. Attempts left:", 3 - attempts)
    print("Student account locked due to 3 wrong attempts.")
    return False

def exam_rules():
    print("Exam Rules:")
    print("1. The exam consists of multiple-choice questions.")
    print("2. Each question has four options: A, B, C, and D.")
    print("3. Enter A, B, C, or D to answer a question.")
    print("4. Enter S to skip a question.")
    print("5. Enter SUBMIT to end exam early.")
    print("6. Each correct answer gives 4 marks.")
    print("7. Each wrong answer deducts 1 mark.")
    print("8. Skipped questions give 0 marks.")
    print("9. Exam will auto-submit when all questions are attempted.")

def get_student_information():
    student_name = input("Enter student full name: ")
    roll_number = input("Enter roll number: ")
    if empty_check(student_name) or empty_check(roll_number):
        print("Name and roll number cannot be empty.")
        return {}
    student_info = {
        "name": student_name,
        "roll_number": roll_number
    }
    return student_info

def start_exam(student_info):
    if len(questions) == 0:
        print("No questions available for exam.")
        return {}

    answered_questions = {}
    skipped_questions = []
    detailed_answers = []
    correct_answers = 0
    wrong_answers = 0
    skipped_count = 0
    marks = 0
    question_number = 1

    print("Starting exam...")
    time.sleep(1)

    for question in questions:
        print("----------------------------------------")
        print("Question No:", question_number)
        print("Subject:", question["subject"])
        print(question["question"])
        print("A. " + question["A"])
        print("B. " + question["B"])
        print("C. " + question["C"])
        print("D. " + question["D"])

        while True:
            answer = input("Enter your answer (A, B, C, D, S for skip, or SUBMIT): ").upper()
            if answer in ["A", "B", "C", "D", "S", "SUBMIT"]:
                break
            else:
                print("Invalid answer. Please enter A, B, C, D, S, or SUBMIT.")

        if answer == "SUBMIT":
            print("Exam submitted early.")
            break
        elif answer == "S":
            print("Question skipped.")
            skipped_questions.append(question["question"])
            skipped_count = skipped_count + 1
            detailed_answers.append({
                "question": question["question"],
                "student_answer": "Skipped",
                "correct_answer": question["answer"],
                "status": "Skipped"
            })
        else:
            answered_questions[question["question"]] = answer
            if answer == question["answer"]:
                marks = marks + 4
                correct_answers = correct_answers + 1
                status = "Correct"
            else:
                marks = marks - 1
                wrong_answers = wrong_answers + 1
                status = "Wrong"
            detailed_answers.append({
                "question": question["question"],
                "student_answer": answer,
                "correct_answer": question["answer"],
                "status": status
            })

        question_number = question_number + 1

    remaining_questions = len(questions) - len(detailed_answers)
    if remaining_questions > 0:
        for index in range(remaining_questions):
            skipped_count = skipped_count + 1
            question = questions[len(detailed_answers)]
            detailed_answers.append({
                "question": question["question"],
                "student_answer": "Skipped",
                "correct_answer": question["answer"],
                "status": "Skipped"
            })

    total_marks = len(questions) * 4
    percentage = (marks / total_marks) * 100
    percentage = round(percentage, 2)
    grade = calculate_grade(percentage)
    date_time = time.strftime("%d-%m-%Y %I:%M:%S %p")

    result = {
        "name": student_info["name"],
        "roll_number": student_info["roll_number"],
        "date_time": date_time,
        "score": marks,
        "correct": correct_answers,
        "wrong": wrong_answers,
        "skipped": skipped_count,
        "percentage": percentage,
        "grade": grade,
        "answers": detailed_answers
    }

    student_marks[student_info["roll_number"]] = marks
    student_results.append(result)
    submit_exam()
    print_student_result(result)
    return result

def submit_exam():
    print("Submitting your exam...")
    time.sleep(1)
    print("Exam submitted successfully!")

def print_student_result(result):
    print("----------------------------------------")
    print("Result")
    print("Name:", result["name"])
    print("Roll Number:", result["roll_number"])
    print("Exam Date/Time:", result["date_time"])
    print("Total Score:", result["score"])
    print("Correct Answers:", result["correct"])
    print("Wrong Answers:", result["wrong"])
    print("Skipped Questions:", result["skipped"])
    print("Percentage:", str(result["percentage"]) + "%")
    print("Grade:", result["grade"])

def review_answers(result):
    print("----------------------------------------")
    print("Detailed Result Review")
    question_number = 1
    for answer in result["answers"]:
        print("----------------------------------------")
        print("Question No:", question_number)
        print(answer["question"])
        print("Student Answer:", answer["student_answer"])
        print("Correct Answer:", answer["correct_answer"])
        print("Status:", answer["status"])
        question_number = question_number + 1

def view_my_result(roll_number):
    found = False
    for result in student_results:
        if result["roll_number"] == roll_number:
            found = True
            print_student_result(result)
    if found == False:
        print("No result found.")

def view_my_detailed_result(roll_number):
    found = False
    for result in student_results:
        if result["roll_number"] == roll_number:
            found = True
            review_answers(result)
    if found == False:
        print("No result found.")

#Main program loop
while True:
    print("----------------------------------------")
    print("Welcome to the Exam E-CAT!")
    print("Please select your user type:")
    print("1. Admin")
    print("2. Student")
    print("3. Exit")
    user_type = input("Enter your choice (1-3): ")

    #Admin login and menu
    if user_type == "1":
        if admin_login():
            while True:
                print("----------------------------------------")
                print("Admin Menu:")
                print("1. View Questions")
                print("2. Add Question")
                print("3. Delete Question")
                print("4. Update Question")
                print("5. Question Bank Statistics")
                print("6. View All Student Results")
                print("7. View Detailed Result Per Student")
                print("8. Class Result Statistics")
                print("9. Exit Admin Menu")
                admin_choice = input("Enter your choice (1-9): ")

                if admin_choice == "1":
                    view_questions(questions)
                elif admin_choice == "2":
                    add_question(questions)
                elif admin_choice == "3":
                    delete_question(questions)
                elif admin_choice == "4":
                    update_question(questions)
                elif admin_choice == "5":
                    question_bank_statistics(questions)
                elif admin_choice == "6":
                    view_all_student_results()
                elif admin_choice == "7":
                    view_detailed_result_per_student()
                elif admin_choice == "8":
                    class_result_statistics()
                elif admin_choice == "9":
                    print("Exiting Admin Menu.")
                    break
                else:
                    print("Invalid choice. Please try again.")
                time.sleep(1)

    #Student login and menu
    elif user_type == "2":
        if student_login():
            student_info = get_student_information()
            if student_info != {}:
                last_result = {}
                while True:
                    print("----------------------------------------")
                    print("Student Menu:")
                    print("1. Show Exam Rules")
                    print("2. Start Exam")
                    print("3. View My Result")
                    print("4. Review My Answers")
                    print("5. Exit Student Menu")
                    student_choice = input("Enter your choice (1-5): ")

                    if student_choice == "1":
                        exam_rules()
                    elif student_choice == "2":
                        exam_rules()
                        start_choice = input("Do you want to start exam now? (yes/no): ").lower()
                        if start_choice == "yes":
                            last_result = start_exam(student_info)
                        elif start_choice == "no":
                            print("Exam not started.")
                        else:
                            print("Invalid choice.")
                    elif student_choice == "3":
                        view_my_result(student_info["roll_number"])
                    elif student_choice == "4":
                        if last_result != {}:
                            review_answers(last_result)
                        else:
                            view_my_detailed_result(student_info["roll_number"])
                    elif student_choice == "5":
                        print("Exiting Student Menu.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
                    time.sleep(1)
    elif user_type == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
