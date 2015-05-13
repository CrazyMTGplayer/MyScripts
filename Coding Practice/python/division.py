#divison.py
#Write a funtion, which given 2 integers, prints the first N digits of the rational number
#5/3 with N = 5, 1.66666, N = 2, 1.66

def main():
	inputstring = raw_input('Enter inputs here (num den digits): ')
	print "Input is ",  inputstring
	print "Output is ", process(inputstring)

def process(data):
	inputs = data.split()
	ints, outs = [], []
	for numbers in inputs:
		ints.append(int(numbers))

	outs.append(ints[0]/ints[1])
	outs.append('.')

	while (ints[2] > 0):
		ints[0] = (ints[0] % ints[1]) * 10
		outs.append(ints[0]/ints[1])
		ints[2] -= 1

	return ''.join(str(things) for things in outs)

if __name__ == "__main__":
	main()

