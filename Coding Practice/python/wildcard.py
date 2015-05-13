#wildcard.py
#? is wildcard. Print all combinations of 01?
# 010, 011

def main():
	inputstring = raw_input('Enter inputs here: ')
	print "Input is ",  inputstring
	print "Output is "
	process(inputstring, 0)

def process(data, cursor):
	if (len(data) == cursor):
		print data
		return

	if (data[cursor] == '?'):
		process(data[:cursor] + '0' + data[cursor + 1:], cursor + 1)
		process(data[:cursor] + '1' + data[cursor + 1:], cursor + 1)
	else:
		process(data, cursor + 1)

if __name__ == "__main__":
	main()

