# Grade calculation script

# Ask for student's name
name = input("Enter student's name: ")

# Ask for 3 subject marks
marks = []
for i in range(1, 4):
    while True:
        try:
            mark = float(input(f"Enter mark for subject {i}: "))
            marks.append(mark)
            break
        except ValueError:
            print("Please enter a valid number.")

# Calculate average
average = sum(marks) / len(marks)

# Display result
print("----------------------")
print(f"\nStudent: {name}")
print(f"Average marks: {average:.2f}")
if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
print("----------------------")
