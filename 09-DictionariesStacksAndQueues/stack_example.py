import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
stack = queue.LifoQueue()

# adds elements to the top of the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8) 

last_one = stack.get()
second_last = stack.get()

sum_last_two = last_one + second_last
print(f"Suma ostatni dwóch liczb: {sum_last_two}")
## prints number of elements of the stack
remaining_sum = 0

# removes and prints elements from the top of the stack
while not stack.empty():
    number = stack.get()
    remaining_sum += number

print(f"Suma pozostałych elementow: {remaining_sum}")

"""
Note the order of the printed elements.
The last added element is printed first.
"""
