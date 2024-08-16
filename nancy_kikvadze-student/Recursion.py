"""Here are Python examples of recursion applied in both frontend-related tasks (like nested data rendering)
 and backend tasks (like directory traversal and sorting algorithms):"""

"""1. Frontend Use Case: Rendering Nested Comments
This example mimics how nested comments could be rendered in Python, similar to what you might do in a frontend framework:"""

comments = {
    "text": "Main comment",
    "replies": [
        {
            "text": "First reply",
            "replies": [
                {"text": "Reply to first reply", "replies": []},
                {"text": "Another reply", "replies": []},
            ]
        },
        {"text": "Second reply", "replies": []},
    ]
}

def render_comments(comment, depth=0):
    print("  " * depth + comment["text"])
    for reply in comment.get("replies", []):
        render_comments(reply, depth + 1)

render_comments(comments)


"""Output:"""
"""Main comment
  First reply
    Reply to first reply
    Another reply
  Second reply"""


"""2. Backend Use Case: Directory Traversal
This is an example of recursively traversing directories and printing out all file paths:"""



import os

def list_files(dir_path):
    for entry in os.listdir(dir_path):
        full_path = os.path.join(dir_path, entry)
        if os.path.isdir(full_path):
            # If it's a directory, recurse into it
            list_files(full_path)
        else:
            # If it's a file, print the path
            print(full_path)

list_files('/path/to/directory')

"""This script will traverse the directory and all subdirectories, printing the path of every file.

3. Backend Use Case: Recursive Sorting (Quicksort)
Here's a classic example of using recursion to implement quicksort:"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

unsorted_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort(unsorted_list)
print(sorted_list)

"""Output:

csharp
Copy code
[1, 1, 2, 3, 6, 8, 10]
4. Backend Use Case: Recursive Tree Traversal (Depth-First Search)
If you have a tree structure, you can traverse it recursively. Here’s a simple tree traversal using Depth-First Search (DFS):"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def traverse_tree(node):
    print(node.value)  # Process the node
    for child in node.children:
        traverse_tree(child)  # Recursively traverse children

# Example tree
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3), TreeNode(4)]
root.children[0].children = [TreeNode(5), TreeNode(6)]

traverse_tree(root)


"""Output:

Copy code
1
2
5
6
3
4


5. Database-Like Recursive Function: Fibonacci Sequence
A famous example of recursion is calculating the Fibonacci sequence:"""
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))


"""Output:

Copy code
0
1
1
2
3
5
8
13
21
34
Summary
Recursion is an essential tool in Python, enabling elegant 
solutions for problems involving hierarchical data, complex sorting, and more.
Whether in the frontend or backend, it's a powerful pattern worth mastering."""












