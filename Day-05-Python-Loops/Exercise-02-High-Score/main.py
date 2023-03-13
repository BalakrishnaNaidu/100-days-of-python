"""calculates the highest score from a List of scores."""


def main():
    """calculates the highest score from a List of scores."""

    # 🚨 Don't change the code below 👇
    student_scores = input("Input a list of student scores ").split()

    for n, _ in enumerate(student_scores):
        student_scores[n] = int(student_scores[n])
    print(student_scores)
    # 🚨 Don't change the code above 👆

    # Write your code below this row 👇

    # Initialize the first element of the list as max value

    max_value = student_scores[0]

    for score in student_scores:
        if score > max_value:
            max_value = score

    print(f"The highest score in the class is: {max_value}")


if __name__ == "__main__":
    main()
