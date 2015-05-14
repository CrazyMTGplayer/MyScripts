#fiborecursive.py
#places first 100 fibo in a list, done iteratively
#[1,1,2,3,5,8,13,21,etc]

def main():
	inputstring = raw_input('Enter nth Fibo to find: ')
	print "Input is ",  inputstring
	print "Output is ", process(int(inputstring))

def process(iteration):
	out = []
	for num in range(iteration):
		if num == 1 or num == 0:
			out.append(1)
		else:
			out.append(out[num-1] + out[num-2])
	return out

if __name__ == "__main__":
	main()

