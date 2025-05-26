def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for problem in problems:
        parts = problem.split()
        operand1, operator, operand2 = parts

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_len = max(len(operand1), len(operand2)) + 2

        line1 += operand1.rjust(max_len) + "    "
        line2 += operator + operand2.rjust(max_len - 1) + "    "
        line3 += "-" * max_len + "    "
        line4 += str(eval(problem)).rjust(max_len) + "    " if show_answers else ""

    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

    if show_answers:
        arranged_problems += "\n" + line4.rstrip()

    return arranged_problems


# Example usage:
print("\nProblems List:")
print(f'1. \n {arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'2. \n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'3. \n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'4. \n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'5. \n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'6. \n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'7. \n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'8. \n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'9. \n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'10. \n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')


