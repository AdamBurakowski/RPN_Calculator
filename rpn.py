correct = False
while not correct:
    answer = input("Show explanation of what the program does, and how to use it? y/n: ")
    print(answer)
    if(answer.lower() == "y"):
        correct = True
        print("""This program is translating postfix Reverse  Polish Notation
into more commonly used infix notation, and computes the equation\n""")
        print("""The program works for addition (+), subtraction (-),
multiplication (*), division (/), modulo  (%), and rising to the power (^)""")
        print("""You start by putting operands and the operators go after them.
        For example 1 2 + is 1 + 2 or „take 1 and 2... add them tohether”""")
        print("""It is possible to stack operators. 1 2 3 ++ is the same as
1 2 + 3 + or 1 + 2 + 3""")
        print("""Correct syntax is: \"operands with spaces in between them\"\"space\"\"operators\"\n""")
    elif(answer.lower() == "n"):
        correct = True
    else:
        print("Input incorrect please try again")

valid_operands = "1234567890."
valid_operators = "+-*/%^"


def operate(arg):
    operation = []
    org_len = len(arg)
    translated_equation = []
    stack = []
    a,b = "", ""

    for e in arg:
        if e not in valid_operators:
            stack.append(e)
        else:
            if len(stack) < 2:
                print("Incorrectly placed operator detected... equation REJECTED")
                exit()
            if e == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(float(a) + float(b))
                # if translated_equation:
                #     translated_equation.append(f"({translated_equation.pop()} + {a})")
                # else:
                translated_equation.append(f"({a} + {b})")
            elif e == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(float(a) - float(b))
                # if translated_equation:
                #     translated_equation.append(f"({translated_equation.pop()} - {a})")
                # else:
                translated_equation.append(f"({a} - {b})")
            elif e == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(float(a) * float(b))
                # if translated_equation:
                #     translated_equation.append(f"({translated_equation.pop()} * {a})")
                # else:
                translated_equation.append(f"({a} * {b})")
            elif e == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(float(a) / float(b))
                # if translated_equation:
                #     translated_equation.append(f"({translated_equation.pop()} / {a})")
                # else:
                translated_equation.append(f"({a} / {b})")
            elif e == "%":
                b = stack.pop()
                a = stack.pop()
                stack.append(float(a) % float(b))
                translated_equation.append(f"({a} % {b})")
            elif e == "^":
                b = stack.pop()
                a = stack.pop()
                stack.append(float(a) ** float(b))
                translated_equation.append(f"({a} ^ {b})")

    return stack, translated_equation


def main():
    infix_equation = []
    postfix_equation = input("enter your prefix equation (leaving this field empty exits the program):\n")
    if(postfix_equation == ""):
        exit()

    postfix_equation = postfix_equation.rstrip()
    operand = ""
    operators_and_operands = []
    i = 0

    while i <  len(postfix_equation):
        char = postfix_equation[i]
        if i < len(postfix_equation) - 1:
            next_element = postfix_equation[i+1]
        if(char == "-" and next_element in valid_operands):
            for j in range(i+1, len(postfix_equation) - 1):
                if (postfix_equation[j] in valid_operands):
                    operand += postfix_equation[j]
                else:
                    operators_and_operands.append("-"+operand)
                    operand = ""
                    i = j
                    break
            continue
        if(postfix_equation[i] in valid_operators):
            operators_and_operands.append(char)
        elif(postfix_equation[i] in valid_operands):
            operand += char
        elif(postfix_equation[i] == " "):
            if(operand != ""):
                operators_and_operands.append(operand)
                operand = ""
        else:
            print("Invalid character detected... equation REJECTED")
            exit()
        i += 1

    if(operand != ""):
        print("Orphaned operand detected... equation REJECTED")
        exit()

    if(operators_and_operands[0][0] not in valid_operands and operators_and_operands[0][0] != "-"):
        print("Operator at the start detected... equation REJECTED")
        exit()

    print(operators_and_operands)

    while (len(operators_and_operands) != 1) or valid_operators in operators_and_operands:
        operators_and_operands, infix_equation = operate(operators_and_operands)

    if(len(operators_and_operands) != 1):
        print("Not enough operators  detected... equation REJECTED")
        exit()

    print(f"In infix notation that would be: {infix_equation}")
    print(f"This equation is equal to: {operators_and_operands[0]}")
    exit()

if __name__ == "__main__":
    main()

