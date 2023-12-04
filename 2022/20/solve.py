data = [int(l.strip()) for l in open('data.txt')]

class Node:
    def __init__(self, idx, value) -> None:
        self.idx = idx
        self.value = value
        self.next = None
        self.prev = None

def remove_next(node):
    deleted = node.next
    deleted.next.prev = node
    node.next = deleted.next

def insert_after(node, new_node):
    next_node = node.next
    node.next = new_node
    new_node.prev = node
    new_node.next = next_node
    next_node.prev = new_node

def move(node, n):
    current = node.prev
    remove_next(current)
    for _ in range(abs(n)): current = current.next if n > 0 else current.prev
    insert_after(current, node)

def find_value(root, pred):
    current = root
    while not pred(current): current = current.next
    return current

def mix(root):
    current = root
    for i in range(len(data)):
        current = find_value(current, lambda x: x.idx == i)
        n = current.value % (len(data) - 1) if current.value >= 0 else -(abs(current.value) % (len(data) - 1))
        move(current, n)

def full_mix(key, iter):
    root = Node(0, data[0] * key)
    last_node = root
    for i in range(1, len(data)):
        current = Node(i, data[i] * key)
        last_node.next = current
        current.prev = last_node
        last_node = current
    last_node.next = root
    root.prev = last_node
    for _ in range(iter): mix(root)
    res, root = 0, find_value(root, lambda x: x.value == 0)
    current = root
    for _ in range(1000): current = current.next
    res += current.value
    for _ in range(1000): current = current.next
    res += current.value
    for _ in range(1000): current = current.next
    res += current.value
    return res

print(full_mix(1, 1))
print(full_mix(811589153, 10))