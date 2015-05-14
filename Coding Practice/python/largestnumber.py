#https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
#largestnumber.py
#list of non negative numbers and arrange to make largest possible number
#in:[50 2 1 9] out: [95021]

def main():
	inputstring = raw_input('Enter inputs here: ')
	print "Input is ",  inputstring

	if inputstring == '':
		inputstring = [50, 2, 1, 9]
	else:
		inputstring = map(int, inputstring.split())

	print "Output is ", process(inputstring)

def process(data):
	out = sorted(map(str, data), cmp = lambda a,b: cmp(a+b, b+a), reverse = True)
	return int(''.join(out))

if __name__ == "__main__":
	main()

