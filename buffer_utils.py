from collections import deque, Counter

def create_buffer(size):
    return deque(maxlen=size)

def append_to_buffer(buffer, item):
    buffer.append(item)

def get_most_common(buffer):
    most_common, count = Counter(buffer).most_common(1)[0]
    return most_common, count
