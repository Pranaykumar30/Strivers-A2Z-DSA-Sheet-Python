def sortedInsert(stack, item):
    if len(stack) == 0 or item > stack[-1]:
        stack.append(item)
    else:
        temp = stack.pop()
        sortedInsert(stack, item)
        stack.append(temp)

def sortStack(stack):
    if len(stack) > 0:
        temp = stack.pop()
        sortStack(stack)
        sortedInsert(stack, temp)

def sortAllStacks(stacks):
    sorted_stacks = []
    for stack in stacks:
        sortStack(stack)
        sorted_stacks.append("".join(map(str, stack)))
    return sorted_stacks