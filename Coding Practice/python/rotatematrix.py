#https://blog.svpino.com/2015/05/10/programming-challenge-rotating-a-matrix-90-degrees-in-place
#rotatematrix.py
#rotate a matrix 90 degrees in the same matrix
#i technically created a new matrix

def main():
	print "inputs delimited with a space"
	first = raw_input('Enter inputs here: ')
	first = first.split()
	size = len(first)
	
	matrix = []
	matrix.append(first)

	while len(matrix) != size:
		row = raw_input('Enter ' + str(len(matrix)+1)  +
		  'th row with lenth of ' + str(size) +': ')
		row = row.split()
		if len(row) == size:
			matrix.append(row)

	for rows in matrix:
		print rows

	print "Output is "
	for rows in process(matrix):
		print rows

def process(data):
	return zip(*data[::-1])

if __name__ == "__main__":
	main()

