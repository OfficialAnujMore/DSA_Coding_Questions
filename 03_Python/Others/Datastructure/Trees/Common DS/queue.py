def createQueue():
    queue = []
    return queue


def isEmpty(queue):
    if len(queue) == 0:
        return True


def enqueue(queue,ele):   
    queue.append(ele)
    # i+=1
    return queue

def dequeue(queue):
    if isEmpty(queue):
        return "Queue is empty"
    else:
        queue.pop(0) 
        return queue

# i = 0
queue = createQueue()
print(enqueue(queue,20))
print(enqueue(queue,2))
print(enqueue(queue,30))
print(dequeue(queue))
# print(queue)


