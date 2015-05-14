#https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
#sumloop.py
#three ways to sum a list, for, while, recursive

def main():
	inputstring = raw_input('Enter inputs here (num broken by spaces): ')
	print "Input is ",  inputstring
	inputlist = makeList(inputstring)
	print "Output for is ", process1(inputlist)
	print "Output while is ", process2(inputlist)
	print "Output recursive is ", process3(inputlist)

def makeList(data):
	return data.split()

def process1(data):
	out = 0
	for num in data:
		out += int(num)
	return out

def process2(data):
	out, count = 0, 1
	while count <= len(data):
		out += int(data[count -1])
		count += 1
	return out

def process3(data):
	if data == []:
		return 0
	return int(data[0]) + process3(data[1:])

if __name__ == "__main__":
	main()

