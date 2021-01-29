import time
import random
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tix_sold = []

        for i in range(10):
            pq.enqueue('cinefan #' + str(i))

        t_end = time.time() + till_show
        now = time.time()
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)

        return tix_sold

print()

print('Challenge 1')
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
        

new_stack = Stack()
for c in 'beforeyesterday':
    new_stack.push(c)

reverse = ''

for i in range(len(new_stack.items)):
    reverse += new_stack.pop()
print(reverse)

print()

print('Challenge 2')
new_list = []
for i in range(1,6):
    new_list.append(i)

print(new_list)

new_stack2 = Stack()
for i in new_list:
    new_stack2.push(i)

back_list = []
for i in range(len(new_stack2.items)):
    back_list.append(new_stack2.pop())
print(back_list)
