
import os
import logging
from collections import defaultdict

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

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
                line_data = line.strip().split(";")
                if len(line_data) != 3:
                    continue
                _, group, grades = line_data
                grades_list = list(map(int, grades.split(",")))
            except ValueError:
                logger.warning(f"Skipping malformed line: {line.strip()}")
                continue

            group_count[group] += 1
            group_grades[group].extend(grades_list)

        group_avg = {
            group: round(sum(grades) / len(grades), 2)
            for group, grades in group_grades.items()
        }

        logger.info(f"Total students: {total_students}")
        logger.info(f"Students per group: {dict(group_count)}")
        logger.info(f"Average grade per group: {group_avg}")

        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n--- Statistics ---\n")
            f.write(f"Total students: {total_students}\n")
            f.write(f"Students per group: {dict(group_count)}\n")
            f.write(f"Average grade per group: {group_avg}\n")

    except FileNotFoundError:
        logger.error("File not found")
    except PermissionError:
        logger.error("Permission denied")
    except ValueError as e:
        logger.error(f"Validation error: {e}")
    except Exception as e:
        logger.exception("An unexpected error occurred")

if __name__ == "__main__":
    main()
