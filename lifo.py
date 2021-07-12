a = input('Введите строку: ')
stack = []
fl = True
for lt in a:
    if lt in '({[':
        stack.append(lt)
    elif lt in ')}]':
        if not len(stack):
            fl = False
            break

        br = stack.pop()
        if br == '(' and lt == ')':
            continue
        if br == '[' and lt == ']':
            continue
        if br == '{' and lt == '}':
            continue

        fl = False
        break

print('Good' if fl and not len(stack) else 'Bad')
