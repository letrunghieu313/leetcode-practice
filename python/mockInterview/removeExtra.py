def removeExtra(test):
    stack = []
    remove = []

    for i, ch in enumerate(test):
        if ch == "(":
            stack.append(i)
        elif ch == ")":
            if stack:
                stack.pop()
            else:
                remove.append(i)

    for i in stack:
        remove.append(i)

    result = ""
    for i, ch in enumerate(test):
        if i not in remove:
            result += ch

    return result


s = "lee(t(c)o)de)"
print(removeExtra(s))

