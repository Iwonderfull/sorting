def is_valid_brackets_fifo(s):
    stack = []
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            if char == ')' and stack[-1] == '(' or char == '}' and stack[-1] == '{' or char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack

# Пример использования
input_str = "{([])}"
print(is_valid_brackets_fifo(input_str))  # Результат для FIFO
