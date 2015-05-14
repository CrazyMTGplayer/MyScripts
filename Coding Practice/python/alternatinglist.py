#https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
#alternatinglist.py
#takes 2 lists and creates new list of alternating elements
#[1,2,3] [a,b,c] >> [1,a,2,b,3,c]

def main():
	inputstring1 = raw_input('Enter first array here: ')
	inputstring2 = raw_input('Enter second array here: ')
	print "Input is ",  inputstring1, inputstring2
	print "Output is ", process(inputstring1, inputstring2)

def process(array1, array2):
	list1, list2 = array1.split(), array2.split()
	out = []

	for (num1, num2) in zip(list1, list2):
		out.append(num1)
		out.append(num2)

	return out

if __name__ == "__main__":
	main()

