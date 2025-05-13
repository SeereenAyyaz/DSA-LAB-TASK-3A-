import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def huffman_encoding(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    huffman_codes = {}
    def generate_codes(node, current_code=""):
        if node:
            if node.char is not None:  # Leaf node
                huffman_codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")

    root = priority_queue[0]
    generate_codes(root)

    return huffman_codes

