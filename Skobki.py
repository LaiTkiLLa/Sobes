from Stack import Stack

def balance(some_list):
    stack = Stack()
    for elem in some_list:
        if elem in '([{':
            stack.push(elem)
        elif elem in '}])':
            open_braket = stack.pop()
            if open_braket == '(' and elem == ')':
                continue
            if open_braket == '[' and elem == ']':
                continue
            if open_braket == '{' and elem == '}':
                continue

    return stack.isEmpty()


print(balance('([{}])'))