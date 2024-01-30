
print("Enter your row")
str = input()

def ValidVeirfy(str):
    stack = []
    verify = True

    for temp in str:
        if temp in "([{":
            stack.append(temp)
        elif temp in ")]}":
            if len(stack) == 0:
                verify = False
                break
            br = stack.pop()
            if br == '(' and temp == ')':
                continue
            if br == '[' and temp == ']':
                continue
            if br == '{' and temp == '}':
                continue

            verify = False
            break

    if verify and len(stack) == 0:
        print("Yes")
    else:
        print("No")

ValidVeirfy(str)


