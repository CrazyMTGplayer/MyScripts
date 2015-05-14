#nosortmissingint.py
#given unsorted list of ints from 0-9
#find missing ints
#in: [9,2,1,0,3,5,6] out: [4,7,8]
#no collections (hashtables)

def main():
	inputstring = raw_input('Enter inputs here : ')
	print "Input is ",  inputstring

	if inputstring == '':
		inputstring = [9,2,1,0,3,5,6]
	else:
		inputstring = map(int, inputstring.split())

	print "Output is ", process(inputstring)

def process(data):
	out = [0,1,2,3,4,5,6,7,8,9]
	for num in data:
		find = out.index(num)
		out = out[:find] + out[find+1:]
	return out

if __name__ == "__main__":
	main()

