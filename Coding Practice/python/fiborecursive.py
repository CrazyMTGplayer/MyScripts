#https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
#fibo.py
#computes first 100 fibo nmbers
#1,1,2,3,5,8,13,21,etc

def main():
	inputstring = raw_input('Enter nth Fibo to find: ')
	print "Input is ",  inputstring
	print "Output is ", process(int(inputstring))

def process(iteration):
	if iteration == 2 or iteration == 1:
		return 1
	return process(iteration - 1) + process(iteration -2)

if __name__ == "__main__":
	main()

