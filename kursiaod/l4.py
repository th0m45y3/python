# новый класс для стека
class Stack():
#пустой массив для хранения значений
	def __init__(self):
		print("HOBA TVOYA MAT\n")
		self.array = []
#метод стека – проверка на пустоту массива внутри класса
	def empty(self):
		if len(self.array) == 0:
			return True
		else:
			return False
#метод стека – добавление нового элемента к массиву
	def put(self, item):
		self.array.append(item)

#метод стека – вывод последнего элемента и его удаление в массиве
	def get(self):
		return self.array.pop()

#метод – вывод всех элементов массива из stack, удовлетворяющих условию func (с последнего элемента до первого, при помощи рекурсии)
def pop(stack, func):
	if not stack.empty():
		num = stack.get()
		pop(stack, func)
		if func(num):
			print(num)
		else:
			stack.put(num)

mystack = Stack()
a = float(input("Enter a:\n"))
b = float(input("Enter b:\n"))
#чтение чисел из файла без переноса строки и пробелов и их запись в стек
with open("file.txt", mode="r", encoding="utf-8-sig") as f:
	for lines in f:
		for l in lines.rstrip('\n').split(' '):
			mystack.put(float(l))
print(f"\nLess than {a}:")
pop(mystack, lambda x: x < a)
print(f"\nBetween {a} and {b}:")
pop(mystack, lambda x: x <= b)
print(f"\nMore than {b}:")
pop(mystack, lambda x: x > b)	
