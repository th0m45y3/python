#класс – узел дерева, хранит в себе значение текущего элемента и указание на левый(меньший) и правый(больший) элемент
class Node():
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

#метод поиска значение в узлах дерева
def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right,key)
    return search(root.left,key)

#метод поиска узла дерева с минимальным значением
def min(root):
	if root.left is None: return root
	else: return min(root.left)

#метод удаления узла из дерева
def delete(root, key):
	if root is None:
		return root
	if key < root.val:
		root.left = delete(root.left, key)
	elif(key > root.val):
		root.right = delete(root.right, key)
	else:
		if root.left is None:
			temp = root.right
			root = None
			return temp
		elif root.right is None:
			temp = root.left
			root = None
			return temp
		temp = min(root.right)
		root.val = temp.val
		root.right = delete(root.right, temp.val)
	return root

#метод вставки значения в дерево
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

#метод – вывод узлов дерева в порядке возрастания
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

import random, time
a = random.sample(range(-2147483648, 2147483647), 100000)
#print(f"Generated array:")
#for i in a: print(i)

b = Node(a[0])   #первый сгенерированного массива задаем корнем дерева
for i in range (1, len(a)-1):
    b = insert(b, a[i])   #каждый следующий элемент массива вставляем в дерево
#print(f"\nBinary tree:")
#inorder(b)

k = a[-1]
t = time.time()
search(b, k)
t = (time.time() - t)*1000
print(f"Binary search tree execution time: {t*1000} milliseconds")
t = time.time()
a.index(k)
t = (time.time() - t)*1000
print(f"Python search execution time: {t*1000} milliseconds")
