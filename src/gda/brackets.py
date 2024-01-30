def valid_brack(string):
    stack = []
    open_bracket = ['(', '[', '{']
    close_bracket = [')', ']', '}']
    valid = True
    for i in string:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            if len(stack) == 0:
                valid = False
                break
            brack = stack.pop()
            if (brack == '(' and i == ')') or (brack == '[' and i == ']') or (brack == '{' and i == '}'):
                continue
            else:
                valid = False
                break
    if valid and len(stack) == 0:
        return 'верно'
    else:
        return 'неверно'
brackets_string = input('Введите скобочную последовательность:')
print(brackets_string, '-', valid_brack(brackets_string))
