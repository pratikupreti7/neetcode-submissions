
class MyStack:
    
    def __init__(self):
        self.queue=deque()

    def pop(self):
        return self.queue.popleft()

    def push(self,x):
        self.queue.append(x)

        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def empty(self):
        return not self.queue

    def top(self):
        return self.queue[0]





