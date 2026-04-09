
import os
from collections import defaultdict


def main():
    filename = "students.txt"

    students = [
        "Ivanov;101;8,9,7",
        "Petrov;101;6,7,8",
        "Sidorov;102;9,9,10",
        "Smirnov;102;5,6,7",
    ]

    try:
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(students) + "\n")

        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            raise ValueError("File is empty")

        total_students = len(lines)
        group_count = defaultdict(int)
        group_grades = defaultdict(list)

        for line in lines:
            try:
                _, group, grades = line.strip().split(";")
                grades_list = list(map(int, grades.split(",")))
            except ValueError:
                continue

            group_count[group] += 1
            group_grades[group].extend(grades_list)

        group_avg = {
            group: round(sum(grades) / len(grades), 2)
            for group, grades in group_grades.items()
        }

        print("Total students:", total_students)
        print("Students per group:", dict(group_count))
        print("Average grade per group:", group_avg)

        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n--- Statistics ---\n")
            f.write(f"Total students: {total_students}\n")
            f.write(f"Students per group: {dict(group_count)}\n")
            f.write(f"Average grade per group: {group_avg}\n")

    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
