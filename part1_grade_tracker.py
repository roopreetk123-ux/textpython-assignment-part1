# ================================
# TASK 1: DATA PARSING & CLEANING
# ================================

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

print("\n===== TASK 1: CLEANED STUDENT DATA =====\n")

for student in raw_students:
    # Clean name
    name = student["name"].strip().title()
    
    # Convert roll
    roll = int(student["roll"])
    
    # Convert marks string to list
    marks = [int(x.strip()) for x in student["marks_str"].split(",")]
    
    # Validate name
    is_valid = all(word.isalpha() for word in name.split())
    validation = "✓ Valid name" if is_valid else "✗ Invalid name"
    
    # Store cleaned data
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })
    
    # Print profile
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print(validation)
    print("================================")

# Find roll 103 student
for student in cleaned_students:
    if student["roll"] == 103:
        print("\nSpecial Output:")
        print(student["name"].upper())
        print(student["name"].lower())


# ================================
# TASK 2: MARKS ANALYSIS
# ================================

print("\n===== TASK 2: MARKS ANALYSIS =====\n")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# Grade function
def get_grade(m):
    if 90 <= m <= 100:
        return "A+"
    elif 80 <= m <= 89:
        return "A"
    elif 70 <= m <= 79:
        return "B"
    elif 60 <= m <= 69:
        return "C"
    else:
        return "F"

# Print subjects with grades
for sub, m in zip(subjects, marks):
    print(f"{sub}: {m} ({get_grade(m)})")

# Calculations
total = sum(marks)
average = round(total / len(marks), 2)

max_mark = max(marks)
min_mark = min(marks)

max_sub = subjects[marks.index(max_mark)]
min_sub = subjects[marks.index(min_mark)]

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average}")
print(f"Highest: {max_sub} ({max_mark})")
print(f"Lowest: {min_sub} ({min_mark})")

# While loop for adding subjects
new_subjects = []
new_marks = []

while True:
    sub = input("\nEnter subject name (or 'done'): ")
    
    if sub.lower() == "done":
        break
    
    mark_input = input("Enter marks (0-100): ")
    
    if not mark_input.isdigit():
        print("Invalid input! Enter numeric value.")
        continue
    
    mark = int(mark_input)
    
    if 0 <= mark <= 100:
        new_subjects.append(sub)
        new_marks.append(mark)
    else:
        print("Marks must be between 0 and 100.")

# Update data
all_marks = marks + new_marks

print(f"\nNew subjects added: {len(new_subjects)}")

if len(all_marks) > 0:
    new_avg = round(sum(all_marks) / len(all_marks), 2)
    print(f"Updated Average: {new_avg}")


# ================================
# TASK 3: CLASS PERFORMANCE
# ================================

print("\n===== TASK 3: CLASS PERFORMANCE =====")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
averages = []

topper_name = ""
topper_avg = 0

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    averages.append(avg)
    
    status = "Pass" if avg >= 60 else "Fail"
    
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1
    
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
    
    print(f"{name:<18} | {avg:7} | {status}")

# Final stats
class_avg = round(sum(averages) / len(averages), 2)

print(f"\nPassed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Topper: {topper_name} {topper_avg}")
print(f"Class Average: {class_avg}")


# ================================
# TASK 4: STRING OPERATIONS
# ================================

print("\n===== TASK 4: STRING OPERATIONS =====\n")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1
clean_essay = essay.strip()
print("Clean Essay:", clean_essay)

# Step 2
print("\nTitle Case:", clean_essay.title())

# Step 3
count = clean_essay.count("python")
print("\nCount of 'python':", count)

# Step 4
replaced = clean_essay.replace("python", "Python 🐍")
print("\nReplaced Essay:", replaced)

# Step 5
sentences = clean_essay.split(". ")
print("\nSentences List:", sentences)

# Step 6 (FIXED)
print("\nNumbered Sentences:")
for i, sentence in enumerate(sentences, 1):
    sentence = sentence.strip()
    sentence = sentence.capitalize()
    
    if not sentence.endswith("."):
        sentence += "."
    
    print(f"{i}. {sentence}")


# Prevent auto close (IMPORTANT)
input("\nPress Enter to exit...")
