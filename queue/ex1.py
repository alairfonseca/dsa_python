# create 3 stacks with a single list
NUMBER_OF_STACKS = 3


class MultiStack:
    def __init__(self, stacksize):
        self.list = [0] * (NUMBER_OF_STACKS * stacksize)
        self.sizes = [0] * NUMBER_OF_STACKS
        self.stacksize = stacksize

    def is_full(self, stack_id):
        return self.sizes[stack_id] == self.stacksize

    def is_empyt(self, stack_id):
        return not self.sizes[stack_id]

    def top_index(self, stack_id):
        offset = stack_id * self.stacksize

        return offset + self.sizes[stack_id] - 1

    def push(self, stack_id, value):
        if self.is_full(stack_id):   
            raise Exception("Stack is full")
        else:
            self.sizes[stack_id] += 1
            self.list[self.top_index(stack_id)] = value

    def pop(self, stack_id):
        if self.is_empyt(stack_id):
            raise Exception("Stack is empty")
        else:
            result = self.list[self.top_index(stack_id)]
            self.list[self.top_index(stack_id)] = 0
            self.sizes[stack_id] -= 1

            return result

    def peek(self, stack_id):
        return self.list[self.top_index(stack_id)]

if __name__ == "__main__":
    ms = MultiStack(3)

    print(ms.list)

    ms.push(0, 1)
    ms.push(1, 2)
    ms.push(2, 3)
    print(ms.list)

    ms.push(0, 4)
    ms.push(1, 5)
    ms.push(2, 6)
    print(ms.list)
    
    ms.push(0, 7)
    ms.push(1, 8)
    ms.push(2, 9)
    print(ms.list)

    ms.pop(2)
    ms.pop(0)
    print(ms.list)

    print(ms.peek(0))
    print(ms.peek(1))
    print(ms.peek(2))
