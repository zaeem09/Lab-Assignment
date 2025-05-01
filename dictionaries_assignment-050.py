

# Zaeem Kashif
# SP24-BBA-050
# Section C



# Creating a dictionary with 10 students and their scores
student_scores = {
    "Umer": 85,
    "Ali": 78,
    "Faizan": 92,
    "Ayesha": 88,
    "Usman": 76,
    "Ahmed": 90,
    "Abrar": 95,
    "Abubakr": 80,
    "Zia": 87,
    "Zaeem": 82
}

# No.1. get() - Retrieve the score of a specific student
print("1. Zainab's score is:", student_scores.get("Zainab"))

# No.2. keys() - List all student names
print("2. List of students:", list(student_scores.keys()))

# No.3. values() - List all scores
print("3. Their scores:", list(student_scores.values()))

# No.4. items() - Display all key-value pairs
print("4. Student and score pairs:")
for name, score in student_scores.items():
    print(f"   {name}: {score}")

# No.5. update() - Update a student's score
student_scores.update({"Ali": 89})
print("5. Ali's updated score:", student_scores["Ali"])

# No.6. pop() - Remove a student and return their score
removed_score = student_scores.pop("Usman")
print("6. Usman was removed. His score was:", removed_score)

# No.7. popitem() - Remove the last inserted item
last_entry = student_scores.popitem()
print("7. Last entry removed (likely Nida):", last_entry)

# No.8. copy() - Create a backup copy of the dictionary
scores_backup = student_scores.copy()
print("8. Backup of current student scores:", scores_backup)

# No.9. setdefault() - Add a new student only if they don't exist
student_scores.setdefault("Hira", 81)
print("9. Hira was added with default score. Current list:")
print(student_scores)

# No.10. fromkeys() - Create a new dictionary with default scores
new_students = ["Jawad", "Mina", "Qasim"]
default_scores = dict.fromkeys(new_students, 70)
print("10. New students with default scores:", default_scores)


# clear() - Would remove all items from the dictionary
student_scores.clear()
print("All student data cleared:", student_scores)

