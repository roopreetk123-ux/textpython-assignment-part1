# Grade Tracker Program

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def main():
    print("🎓 Welcome to Grade Tracker")

    num_students = int(input("Enter number of students: "))

    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")

        name = input("Enter student name: ")

        marks = []
        for j in range(3):
            mark = float(input(f"Enter marks for subject {j + 1}: "))
            marks.append(mark)

        total = sum(marks)
        average = total / len(marks)
        grade = calculate_grade(average)

        print("\n📊 Result")
        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")


if __name__ == "__main__":
    main()