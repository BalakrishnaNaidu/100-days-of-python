""""Program to calculate average height of students"""


def main():
    """ Calculate average height"""

    # 🚨 Don't change the code below 👇
    student_heights = input("Input a list of student heights ").split()

    for height, _ in enumerate(student_heights):
        student_heights[height] = int(student_heights[height])
    # 🚨 Don't change the code above 👆

    # Write your code below this row 👇

    # Total height of all students
    total_height = 0
    for height in student_heights:
        total_height += height

    # Total no of students
    num_students = 0
    for _ in student_heights:
        num_students += 1

    # Average = Sum of all studnet height / Number of students
    average = total_height / num_students
    print(round(average))


if __name__ == "__main__":
    main()
