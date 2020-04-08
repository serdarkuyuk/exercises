class Stack:
	def __init__(self):
		self.items = []
	def push(self, item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		if self.items == []:
			return True

	def peek(self):
		return self.items[-1]

	def get_stack(self):
		return self.items

def main():
	arry = Stack()
	arry.push("A")
	arry.push("B")
	arry.push("C")
	arry.push("D")
	print(arry.peek())
	print(arry.get_stack())

if __name__ == '__main__':
	main()
