# Implementation of stack using array


def createStack():
    stack = []
    return stack

def isEmpty(stack):
    if len(stack) == 0:
        return True

def push(stack,ele):
    stack.append(ele)
    return ele , "pushed in stack", stack

def pop(stack):
    if isEmpty(stack):
        return "Stack is empty"
    return stack.pop()

def peek(stack):
    if isEmpty(stack):
        return "Stack is empty"
    return stack[len(stack)-1]


stack = createStack()
print(push(stack,20))
print(push(stack,30))
print(push(stack,50))
print(pop(stack))
print(stack)
print(peek(stack))



