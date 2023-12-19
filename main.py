def calculate_grade(percentage):
    if percentage >= 89:
        return ('A+')
    elif 80 <= percentage <89:
        return 'A'
    elif 70 <= percentage < 79:
        return 'B'
    elif 60 <= percentage < 69:
        return 'C'
    elif 50 <= percentage < 59:
        return 'D'
    else:
        return 'F'
def main():
    name = input("Enter Your Full Name : ")
    num_subjects = int(input("Enter the number of subjects: "))
    total_percentage = 0

    for i in range(1, num_subjects + 1):
        subject_name = input(f"\nEnter the name of subject {i}: ")
        marks = float(input(f"Enter the marks for {subject_name}: "))
        max_marks = 100.0
        percentage = (marks / max_marks) * 100
        grade = calculate_grade(percentage)
        print(f"Subject: {subject_name}, Percentage: {percentage:.2f}%, Grade: {grade}\n")
        total_percentage += percentage
    overall_percentage = total_percentage / num_subjects
    overall_grade = calculate_grade(overall_percentage)
    print(f"\n{name}'s Overall Percentage: {overall_percentage:.2f}% and Overall Grade: {overall_grade}")
if __name__ == "__main__":
    main()




