MIN_LEN = 0


def is_correct_brackets(sequence_brackets):
    stack_brackets = []
    for symbol in sequence_brackets:
        if symbol == '(':
            stack_brackets.append(symbol)
        elif symbol == ')':
            if len(stack_brackets) == MIN_LEN:
                return False
            else:
                stack_brackets.pop()
    return len(stack_brackets) == MIN_LEN


bracket_sequence = input("Введите скобочную последовательность: ")
if is_correct_brackets(bracket_sequence):
    print("правильная скобочная последовательность")
else:
    print("неправильная скобочная последовательность")
