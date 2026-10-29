
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if node is None:
        return 0
    return node.height


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def right_rotate(y):
    x = y.left
    t2 = x.right

    x.right = y
    y.left = t2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    t2 = y.left

    y.left = x
    x.right = t2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    bf = balance_factor(root)

    # LL Case
    if bf > 1 and data < root.left.data:
        return right_rotate(root)

    # RR Case
    if bf < -1 and data > root.right.data:
        return left_rotate(root)

    # LR Case
    if bf > 1 and data > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL Case
    if bf < -1 and data < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def search(root, key):
    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


def find_min(root):
    while root.left:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    if root is None:
        return None

    root.height = 1 + max(height(root.left), height(root.right))
    bf = balance_factor(root)

    # LL Case
    if bf > 1 and balance_factor(root.left) >= 0:
        return right_rotate(root)

    # LR Case
    if bf > 1 and balance_factor(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RR Case
    if bf < -1 and balance_factor(root.right) <= 0:
        return left_rotate(root)

    # RL Case
    if bf < -1 and balance_factor(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = None
values = [10, 20, 30, 40, 50, 25]

for value in values:
    root = insert(root, value)

print("AVL Inorder Traversal:")
inorder(root)

key = 25
if search(root, key):
    print("\n", key, "found in AVL tree")
else:
    print("\n", key, "not found in AVL tree")

root = delete(root, 40)
print("After deleting 40:")
inorder(root)
print()
