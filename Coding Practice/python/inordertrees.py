#inordernodes.py
#given two nodes check if they have the same inorder printing
#TRUE is true FALSE if false

import random

def main():
	tree1 = BinaryTree('B')
	tree1.insertLeft('A')
	tree1.insertRight('C')
	printTree(tree1)

	tree2 = BinaryTree('A')
	tree2.insertRight('B')
	tree2.insertRight('C')
	printTree(tree2)


def process():
	return

class BinaryTree():
	def __init__(self, rootid):
		self.right, self.left = None, None
		self.rootid = rootid
	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def setValue(self, value):
		self.rootid = value
	def getValue(self):
		return self.rootid
	def insertLeft(self, value):
		node = BinaryTree(value)
		if self.left == None:
			self.left = node
		else:
			node.left = self.left
			self.left = node
	def insertRight(self, value):
		node = BinaryTree(value)
		if self.right == None:
			self.right = node
		else:
			node.right = self.right
			self.right = node


def printTree(tree):
	if tree != None:
		printTree(tree.getLeftChild())
		print tree.getValue()
		printTree(tree.getRightChild())

def sameInOrder(tree1, tree2):
		

if __name__ == "__main__":
	main()

